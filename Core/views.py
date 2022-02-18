from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .models import Agendamento
from .forms import AgendamentoModelForm, EquipamentoModelForm, ConsultaAgendamentoForm

# Create your views here.


def index(request):
    if str(request.user) == 'AnonymousUser':
        frase = f'Faça seu login por favor.'
    else:
        frase = f'Seja bem vindo, {request.user}'
    context = {
        'FRASE_USUARIO_LOGADO' : frase
    }
    return render(request, 'index.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(index)

@login_required
def consulta_agenda(request):
    resultados_consulta = ""
    if str(request.method) == 'POST':
        form = ConsultaAgendamentoForm(request.POST or None) 
        if form.is_valid():
            resultados_consulta = Agendamento.objects.filter(Inicio__range=(form.cleaned_data['Inicio'], form.cleaned_data['Fim']), equipamento=form.cleaned_data['equipamento'])
    else:
        form = ConsultaAgendamentoForm()

    context = {
        'form' : form,
        'resultados_consulta': [' \n'.join(str(item).split('+00:00')) for item in resultados_consulta]
    }
    return render(request, 'consulta_agenda.html', context)

@login_required
def novo_agendamento(request):
    if str(request.method) == 'POST':
        form = AgendamentoModelForm(request.POST)
        if form.is_valid():
            conflitos_inicio = Agendamento.objects.filter(Inicio__range=(form.cleaned_data['Inicio'], form.cleaned_data['Fim']), equipamento=form.cleaned_data['equipamento'])
            conflitos_fim = Agendamento.objects.filter(Fim__range=(form.cleaned_data['Inicio'], form.cleaned_data['Fim']), equipamento=form.cleaned_data['equipamento'])
            if not conflitos_inicio and not conflitos_fim: 
                form.save()
                messages.success(request, 'Agendamento salvo com sucesso.')
                form = AgendamentoModelForm()
            else:
                conflitos= [str(item).split(', ') for item in conflitos_inicio]
                conflitos.append( [str(item).split(', ') for item in conflitos_fim] )
                messages.error(request, f'Já existem agendamentos no período selecionado. Por favor tente com outro hórario.')
                messages.error(request, f'{conflitos[0]}')
        else:
            messages.error(request, 'Erro ao salvar agendamento.')
    else:
        form = AgendamentoModelForm()
    user_group = request.user.groups.values_list('name', flat=True)
    print(user_group)
    form.fields['responsavel'].choices = [('', '---------'), (str(request.user), str(request.user)),]
    
    context = {
        'form' : form,
    }
    return render(request, 'novo_agendamento.html', context)

@login_required
def novo_equipamento(request):
    if str(request.method) == 'POST':
        form = EquipamentoModelForm(request.POST, request.FILES)
        if form.is_valid():
            equip = form.save()
            messages.success(request, 'Produto salvo com sucesso.')
            form = EquipamentoModelForm()
        else:
            messages.error(request, 'Erro ao salvar equipamento.')
    else:
        form = EquipamentoModelForm()
    context = {
        'form': form    
    }
    return render(request, 'novo_equipamento.html', context)

