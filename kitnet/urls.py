"""kitnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from kitnet import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imovel/', views.lista_imoveis),
    path('imovel/cadastro/', views.cadastro),
    path('imovel/cadastro/submit', views.submit_cadastro_imovel),
    path('imovel/cadastro/delete/<int:id_imovel>/', views.delete_imovel),
    #path('produto/cadastro/delete/<int:id_produto>/', views.delete_produto),
    path('novo_cliente/', views.cadastro_cliente),
    path('imovel/lista_cliente/', views.lista_cliente),
    path('', RedirectView.as_view(url='/imovel/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

