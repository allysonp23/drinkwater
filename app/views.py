from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . import forms, usuario_services
from .usuario import Usuario

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = forms.UsuarioForm(data=request.POST)
        if form_usuario.is_valid():
            nome = form_usuario.cleaned_data["nome"]
            email = form_usuario.cleaned_data["email"]
            peso = form_usuario.cleaned_data["peso"]
            password = form_usuario.cleaned_data["password"]
            usuario_novo = Usuario(nome=nome, email=email, peso=peso, password=password)
            usuario_services.cadastrar_usuario(usuario_novo)
            return redirect('home')
        
    else:
        form_usuario = UserCreationForm
    return render(request, 'index.html', {'form_usuario': form_usuario})
        
        
        
