from django.contrib import admin
from core.models import Imovel, Cliente
# Register your models here.


class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'metros', 'dormitorios', 'garagem', 'vagas_garagem', 'varanda', 'tipo_contrato', 'valor', 'condicao')
    #search_fields = ('nome', 'metros', 'dormitorios', 'garagem', 'vagas_garagem', 'varanda', 'tipo_contrato', 'valor', 'condicao')
    list_filter = ('usuario', )


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    #search_fields = ('nome', )
    list_filter = ('usuario',)


admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Cliente, ClienteAdmin)

