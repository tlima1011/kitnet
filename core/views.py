from django.shortcuts import render, redirect
from core.models import Imovel, Cliente
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
def alterarImovel(request):
    id_imovel = request.GET.get('id')
    dados = {}
    if id_imovel:
        dados['imovel'] = Imovel.objects.get(id=id_imovel)
    return render( request, 'altera.html', dados)


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
        varanda = request.POST.get('varanda')
        image1 = request.POST.get('image1')
        image2 = request.POST.get('image2')
        image3 = request.POST.get('image3')
        image4 = request.POST.get('image4')
        image5 = request.POST.get('image5')
        tipo_contrato = request.POST.get('tipo_contrato')
        estado = request.POST.get('estado')
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
                                varanda=varanda,
                                image1=image1,
                                image2=image2,
                                image3=image3,
                                image4=image4,
                                image5=image5,
                                tipo_contrato=tipo_contrato,
                                estado=estado,
                                cidade=cidade,
                                valor=valor,
                                condicao=condicao,
                                usuario=usuario
                              )
    return redirect('/')


@login_required(login_url='/login/')
def delete_imovel(request, id_imovel):
    usuario = request.user
    imovel = Imovel.objects.get(id=id_imovel)
    if usuario == imovel.usuario:
        imovel.delete()
    return redirect('/')


@login_required(login_url='/login/')
def cadastro_cliente(request):
    return render(request, 'novo_cliente.html')


@login_required(login_url='/login/')
def lista_cliente(request):
    usuario = request.user
    cliente = Cliente.objects.filter(usuario=usuario)
    dados = {'cliente': cliente}
    return render(request, 'cliente.html', dados)