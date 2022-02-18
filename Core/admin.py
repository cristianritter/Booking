from django.contrib import admin

# Register your models here.
from .models import Equipamento, Agendamento

'''
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "email")

    def nome_completo(self, obj):
        return obj
'''

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "serial_number")

  

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ("responsavel", "Inicio", "Fim")

