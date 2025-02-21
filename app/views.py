from django.shortcuts import render, redirect
from .models import estado, matricula, leiloeiro, anexo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http.response import HttpResponse
from django.contrib.auth import logout as auth_logout

def home(request):
    leiloeiros = leiloeiro.objects.all()
    estados = estado.objects.all()
    matriculas = matricula.objects.all()
    anexos = anexo.objects.all()
    return render (request, 'index.html', {"leiloeiros": leiloeiros})

def salvar(request):
    vnome = request.POST.get("nome")
    vcpf = request.POST.get("cpf")
    vemail = request.POST.get("email")
    vtelefone = request.POST.get("telefone")
    vsite = request.POST.get("site")
    leiloeiro.objects.create(nome=vnome, cpf=vcpf, email=vemail, telefone=vtelefone, site=vsite)    
    leiloeiros = leiloeiro.objects.all()
    return render (request, 'index.html',{"leiloeiros": leiloeiros})

def editar(request, id):
    leiloeiros = leiloeiro.objects.get(id=id)
    return render(request, "update.html",{"leiloeiro": leiloeiros})

def update(request, id):
    vnome = request.POST.get('nome')
    vcpf = request.POST.get("cpf")
    vemail = request.POST.get("email")
    vtelefone = request.POST.get("telefone")
    vsite = request.POST.get("site")    
    leiloeiros = leiloeiro.objects.get(id=id)
    leiloeiros.nome = vnome
    leiloeiros.cpf = vcpf
    leiloeiros.email = vemail
    leiloeiros.telefone = vtelefone
    leiloeiros.site = vsite   
    leiloeiros.save()
    return redirect(home)

def delete(request, id):
    leiloeiros = leiloeiro.objects.get(id=id)
    leiloeiros.delete()
    return redirect(home)


def cadastro(request):
    if request.method == "GET":        
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já tem usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        leiloeiros = leiloeiro.objects.create(nome=username)
        user.save()

        return HttpResponse('Usuário cadastrado com SUUUUUUCESSO!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return HttpResponse('Usuário Autenticado! Vá para a plataforma')
        else:
            return HttpResponse('Email ou Senha inválida')

@login_required(login_url="/auth/plataforma/")    
def plataforma(request):
    anexos = anexo.objects.all()    
    return render (request, 'plataforma.html', {"anexos": anexos})

def form_valid(self, form):
    form.instance.usuario = self.request.user    
    form = super().form_valid(form)
    return redirect(plataforma)

    
def alterar(request):
    varquivo = request.POST.get("arquivo")
    vid_leiloeiro = request.POST.get("id_leiloeiro")  
    
    try:
        leiloeiro_obj = leiloeiro.objects.get(id=vid_leiloeiro)
    except leiloeiro.DoesNotExist:
        return HttpResponse("Leiloeiro não encontrado", status=404)    
   
    anexo.objects.create(arquivo=varquivo, id_leiloeiro=leiloeiro_obj)
    
    anexos = anexo.objects.all()    
    return render(request, 'plataforma.html', {"anexo": anexos})

def logout(request):
    auth_logout(request) 
    return redirect('login')

