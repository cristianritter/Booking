from django.urls import path

from .views import index, consulta_agenda, exclui_agenda, novo_agendamento, novo_equipamento, logout

urlpatterns = [
    path('', index),
    path('index', index),
    path('consulta_agenda', consulta_agenda, name='consulta_agenda'),
    path('exclui_agenda', exclui_agenda, name='exclui_agenda'),
    path('novo_agendamento', novo_agendamento, name='novo_agendamento'),
    path('novo_equipamento', novo_equipamento, name='novo_equipamento'),
    path('logout', logout, name='logout'),
    
]
