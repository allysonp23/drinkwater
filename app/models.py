from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=55, null=False, blank=False)
    email = models.CharField(max_length=55, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'peso']
    
    def __str__(self):
        return self.email
    
