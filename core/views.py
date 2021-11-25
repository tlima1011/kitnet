from django.shortcuts import render, redirect
from core.models import Imovel
# Create your views here.


'''def index(request):
    return redirect('/imovel/')
'''

def lista_imoveis(request):
    #usuario = request.user
    imovel = Imovel.objects.all()
    dados = {'imovel':imovel}
    return render(request, 'imovel.html', dados)

