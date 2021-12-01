from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Imovel(models.Model):
    TIPO_CONTRATO_CHOICES = (
        ('A', 'Aluguel'),
        ('V', 'Venda')
    )

    CONDICAO_CHOICES = (
        ("U", 'Usado'),
        ("N", 'Novo')
    )

    SIMNAO_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Nao')
    )

    ESTADO_CHOICES = (
        ('SP', 'São Paulo'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá' ),
        ("AM", 'Amazonas'),
        ("BA", 'Bahia'),
        ("CE", 'Ceará' ),
        ("DF", 'Distrito Federal'),
        ("ES", 'Espírito Santo'),
        ("GO", 'Goiás'),
        ("MA", 'Maranhão'),
        ("MT", 'Mato Grosso'),
        ("MS", 'Mato Grosso do Sul'),
        ("MG", 'Minas Gerais'),
        ("PA", 'Pará'),
        ("PB", 'Paraíba'),
        ("PR", 'Paraná'),
        ("PE", 'Pernambuco'),
        ("PI", 'Piauí'),
        ("RJ", 'Rio de Janeiro'),
        ("RN", 'Rio Grande do Norte'),
        ("RS", 'Rio Grande do Sul'),
        ("RO", 'Rondônia'),
        ("RR", 'Roraima'),
        ("SC", 'Santa Catarina'),
        ("SE", 'Sergipe'),
        ("TO", 'Tocantins')
    )

    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    endereco = models.CharField(max_length=40, null=False, blank=False, verbose_name='Endereço')
    cep = models.CharField(max_length=7, null=False, blank=False, verbose_name='CEP')
    metros = models.FloatField(verbose_name='Metros')
    dormitorios = models.IntegerField(verbose_name='Dormitórios')
    banheiros = models.IntegerField(verbose_name='Banheiros')
    garagem = models.CharField(max_length=1, choices=SIMNAO_CHOICES, verbose_name='Garagem')
    vagas_garagem = models.IntegerField(verbose_name='Vagas na Garagem', null=True)
    varanda = models.CharField(max_length=1, choices=SIMNAO_CHOICES, verbose_name='Varanda')
    image1 = models.ImageField(upload_to='templates/images', verbose_name='Imagem 1', null=True, blank=True)
    image2 = models.ImageField(upload_to='templates/images', verbose_name='Imagem 2', null=True, blank=True)
    image3 = models.ImageField(upload_to='templates/images', verbose_name='Imagem 3', null=True, blank=True)
    image4 = models.ImageField(upload_to='templates/images', verbose_name='Imagem 4', null=True, blank=True)
    image5 = models.ImageField(upload_to='templates/images', verbose_name='Imagem 5', null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now=True, verbose_name='Data Inclusao')
    tipo_contrato = models.CharField(max_length=1, choices=TIPO_CONTRATO_CHOICES, blank=False, null=False, verbose_name='Tipo Contrato')
    cidade = models.CharField(max_length=50, null=False, blank=False, verbose_name='Cidade')
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, blank=False, verbose_name='Estado')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    condicao = models.CharField(max_length=1, choices=CONDICAO_CHOICES, verbose_name='Condição')
    #cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='cliente')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'imovel'

    def __str__(self):
        return self.nome

    def get_data_inclusao(self):
        return self.data_inclusao.strftime('%d/%m/%Y %H:%M hrs')


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=20)
    telefone = models.CharField(max_length=9)
    data_nascimento = models.DateTimeField(verbose_name='Data de Nascimento')
    data_cadastro = models.DateTimeField(auto_now=True, verbose_name='Data de Inclusão')
    imovel = models.ForeignKey(Imovel, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y')

    def get_data_cadastro(self):
        return self.data_cadastro.strftime('%d/%M/%Y')














