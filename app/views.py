from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method != "POST":
        return render (request, 'app/index.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    peso = request.POST.get('peso')
    
    if not usuario or not usuario or not senha \
            or not senha2 or not peso:
        messages.error(request, 'Nenhum campo pode estar vazio')
        return render(request, 'app/index.html')
    
    if len(senha) < 6:
        messages.error(request, 'Senha precisar ter pelo menos 6 caracteres!')
        return render(request, 'app/index.html')

    if len(usuario) < 5:
        messages.error(request, 'Usuário precisar ter pelo menos 6 caracteres!')
        return render(request, 'app/index.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem!')
        return render(request, 'app/index.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já cadastrado!')
        return render(request, 'app/index.html')

    messages.success(request, 'Registrado com sucesso! Agora faça seu login!')

    user = User.objects.create_user(username=usuario, password=senha)
    return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request)
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'app/index.html')
    
    else:
        auth.login(request, user)
        messages.sucess(request, 'Você fez login com sucesso!')
        return redirect ('dashboard')
    
def logout(request):
    auth.logout(request)
    return redirect('app/index.html')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'dashboard.html')