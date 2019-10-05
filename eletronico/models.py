from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=100)
    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    cpf = models.CharField(max_length=14, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)


    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.IntegerField()
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField("Lotação", max_length=100)
    responsavel = models.ManyToManyField(Pessoa)

    class Meta:
        verbose_name = "Lotação"
        verbose_name_plural = "Lotações"

    def __str__(self):
        return self.nome

class Processo(models.Model):
    nome = models.CharField("Nome do processo", max_length=200)
    criado_por = models.ForeignKey(
        Funcionario,
        verbose_name="Usuário", 
        on_delete=models.PROTECT,
        related_name="criado_por",
        blank=True,
        null=True
    )
    stakeholders = models.ManyToManyField(
        Pessoa,
        verbose_name = "Interessados",
        related_name="stakeholders",
    )
    investigados = models.ManyToManyField(
        Pessoa,
        related_name="investigados"
    )
    Departamento = models.ForeignKey(
        Departamento,
        verbose_name="Lotação", 
        on_delete=models.PROTECT
    )

class Documento(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    numero = models.IntegerField()
    titulo = models.CharField("Titulo", max_length=200)
    data = models.DateField(auto_now=False, auto_now_add=False)
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.titulo

class Portaria(Documento):
    texto = models.CharField(max_length=100)

class Pedido(Documento):
    justificativa = models.CharField(max_length=50)

class Envio(Documento):
    send_date = models.DateField(auto_now=False, auto_now_add=False)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"

    def __str__(self):
        return self.titulo

class Tramite(models.Model):
    processo = models.ForeignKey(
        Processo, 
        verbose_name="Processo", 
        on_delete=models.PROTECT
    )
    origem = models.ForeignKey(
        Departamento, 
        verbose_name="Saindo de",
        related_name="origem", 
        on_delete=models.PROTECT
    )
    destino = models.ForeignKey(
        Departamento,
        verbose_name="Para",
        related_name="destino",
        on_delete=models.PROTECT
    )
    saida = models.DateTimeField("Saiu em", null=True, blank=True)
    chegada = models.DateTimeField("Chegou em", null=True, blank=True)

    class Meta:
        verbose_name = "Tramite"
        verbose_name_plural = "Tramites"

    def __str__(self):

        return f"{self.processo.nome} - {self.origem.nome} - {self.destino.nome}"

