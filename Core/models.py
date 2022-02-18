from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, timedelta
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

#SIGNALS 
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Criação', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

"""
class Usuario(Base):
    STATUS = (
       ('USER', 'USER'),
       ('STAFF', 'STAFF'),
       ('ADMIN', 'ADMIN'),
    )

    first_name = models.CharField('first_name', max_length=100, blank=True, null=True)
    last_name = models.CharField('last_name', max_length=100, blank=True, null=True)
    login = models.CharField('login', max_length=100, blank=True, null=True)
    email = models.EmailField('email', max_length=100, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True) # validators should be a list
    privilegios = models.IntegerField('privilegios', choices=STATUS, blank=True, null=True)
    password = models.CharField('password', max_length=100, blank=True, null=True)
    password_confirmation = models.CharField('password_confirmation', max_length=100, blank=True, null=True)
    imagem = StdImageField('Imagem', upload_to='usuarios', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

  #  class Meta:
  #      ordering = ("first_name", "last_name")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
"""     

class Equipamento(Base):
    nome = models.CharField('nome', max_length=100, blank=True, null=True)
    marca = models.CharField('marca', max_length=100, blank=True, null=True)
    modelo = models.CharField('modelo', max_length=100, blank=True, null=True)
    descricao = models.CharField('descrição', max_length=200, blank=True, null=True)
    serial_number = models.CharField('serialnumber', max_length=50, blank=True, null=True)
    RFID_tag_id = models.CharField('RFID_tag_id', max_length=50, blank=True, null=True)
    default_locale = models.CharField('default_locale', max_length=50, blank=True, null=True)
    current_locale = models.CharField('current_locale', max_length=50, blank=True, null=True)
    status = models.BooleanField('status', blank=True, null=True)
    imagem = StdImageField('Imagem', upload_to='equipamentos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return f"{self.marca}, {self.modelo}"


class Agendamento(Base):
    Inicio = models.DateTimeField('Data e hora de início da reserva', help_text='Exemplo: 01/01/2020 12:00', default=datetime.now())
    Fim = models.DateTimeField('Data e hora de fim da reserva', help_text='Exemplo: 01/01/2020 13:00', default=datetime.now()+timedelta(hours=1))
    User = get_user_model()
    
    CHOICES_USER = [(str(user),str(user)) for user in User.objects.all()]
    CHOICES_EQUIP = [(str(equip),str(equip)) for equip in Equipamento.objects.all()]
    
    equipamento = models.CharField(max_length=80, choices=CHOICES_EQUIP)
    responsavel = models.CharField(max_length=80, choices=CHOICES_USER)
    
    def __str__(self):
        return f"Equipamento: {self.equipamento}, Responsável: {self.responsavel}, Hora de início: {self.Inicio}, Hora de fim: {self.Fim}"


'''
def usuario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.login)
'''

def equipamento_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


#signals.pre_save.connect(usuario_pre_save, sender=Usuario)
signals.pre_save.connect(equipamento_pre_save, sender=Equipamento)
