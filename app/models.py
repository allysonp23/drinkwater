from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=55, null=False, blank=False)
    email = models.CharField(max_length=55, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'peso']
    
    def __str__(self):
        return self.email
    

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
    
    class Meta:
        abstract = True
        
        
MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStampedModel):
    COPO_1 = 1
    COPO_2 = 2

    INTEGER_CHOICES = (
        (COPO_1, 'Primeiro Valor'),
        (COPO_2, 'Segundo Valor'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    copo = models.CharField(choices=INTEGER_CHOICES, max_length=8)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return str(self.pk)
    
class ConsumoAgua(models.Model):
    COPO_1 = 250
    COPO_2 = 350
    
    INTEGER_CHOICES = (
    (COPO_1, 250),
    (COPO_2, 350),
    )
    data = models.DateTimeField(default=datetime.today)
    quantidade = models.CharField(choices=INTEGER_CHOICES, max_length=8)
    
    class Meta:
        ordering=('pk',)
    
    def __str__(self):
        return '{} - {}'.format(self.pk, self.quantidade)
