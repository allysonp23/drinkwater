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
    
class ConsumoAgua(models.Model): 
    
    TAMANHO_COPO = [
        ("CP", "250"),
        ("CG", "450"),
    ]
    copo_escolhido = models.CharField(max_length=2, choices=TAMANHO_COPO, default='CP')
    dia = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.dia