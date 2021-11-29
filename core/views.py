from django.shortcuts import render, redirect
from core.models import Imovel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha inválido')
    return redirect('/')


@login_required(login_url='/login/')
def lista_imoveis(request):
    usuario = request.user
    imovel = Imovel.objects.filter(usuario=usuario)
    dados = {'imovel':imovel}
    return render(request, 'imovel.html', dados)


@login_required(login_url='/login/')
def cadastro(request):
    return render(request, 'cadastro.html')


@login_required(login_url='/login/')
def submit_cadastro_imovel(request):
    if request.POST:
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cep = request.POST.get('cep')
        metros = request.POST.get('metros')
        dormitorios = request.POST.get('dormitorios')
        banheiros = request.POST.get('banheiros')
        garagem = request.POST.get('garagem')
        vagas_garagem = request.POST.get('vagas_garagem')
        foto1 = request.POST.get('foto1')
        foto2 = request.POST.get('foto2')
        foto3 = request.POST.get('foto3')
        foto4 = request.POST.get('foto4')
        foto5 = request.POST.get('foto5')
        tipo_contrato = request.POST.get('tipo_contrato')
        estado = request.POST.get('estadp')
        cidade = request.POST.get('cidade')
        valor = request.POST.get('valor')
        condicao = request.POST.get('condicao')
        usuario = request.user
        Imovel.objects.create(nome=nome,
                                endereco=endereco,
                                cep=cep,
                                metros=metros ,
                                dormitorios = dormitorios,
                                banheiros =banheiros,
                                garagem = garagem,
                                vagas_garagem=vagas_garagem,
                                foto1=foto1,
                                foto2=foto2,
                                foto3=foto3,
                                foto4=foto4,
                                foto5=foto5,
                                tipo_contrato=tipo_contrato,
                                estado=estado,
                                cidade=cidade,
                                valor=valor,
                                condicao=condicao,
                                usuario=usuario
                              )
        return redirect('/')
    return redirect('/')


@login_required(login_url='/login/')
def cadastro_cliente(request):
    return render(request, 'novo_cliente.html')