from django import forms
from .models import Agendamento, Equipamento
import datetime


class DateTimeWidget(forms.DateTimeInput):
  class Media:
    js = ('js/jquery-ui-timepicker-addon.js',)
  def __init__(self, attrs=None):
    if attrs is not None:
      self.attrs = attrs.copy()
    else:
      self.attrs = {'class': 'datetimepicker'}


class ConsultaAgendamentoForm(forms.Form):

    CHOICES_EQUIP = [(str(equip),str(equip)) for equip in Equipamento.objects.all()]
    CHOICES_EQUIP.insert(0, ('', '----------'))
    equipamento = forms.ChoiceField(choices=CHOICES_EQUIP)
    Inicio = forms.DateField(label = 'Data e hora de inicio', initial=datetime.date.today(), help_text='Preencha um perído de consulta para saber se já existem agendamentos. Exemplo: 01/01/2020 12:00' )
    Fim = forms.DateField(label = 'Data e hora de fim', initial=datetime.date.today()+datetime.timedelta(days=1), help_text='Preencha um perído de consulta para saber se já existem agendamentos. Exemplo: 01/01/2020 13:00')


class ExcluirAgendamentoForm(forms.Form):

    CHOICES_AGEND = [(str(agend),str(agend)) for agend in Agendamento.objects.all()]
    CHOICES_AGEND.insert(0, ('', '----------'))
    agendamento = forms.ChoiceField(choices=CHOICES_AGEND)


class AgendamentoModelForm(forms.ModelForm):
   
    class Meta:
        model = Agendamento
        fields = ['equipamento','Inicio', 'Fim', 'responsavel']
        widgets = {
            #'Inicio': DateTimeWidget()
        }

    
class EquipamentoModelForm(forms.ModelForm):
    
    class Meta:
        model = Equipamento
        fields = ['nome', 'marca', 'modelo', 'descricao', 'serial_number', 'imagem']

