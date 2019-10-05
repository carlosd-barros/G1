from django.contrib import admin
from .models import (
    Pessoa,
    Funcionario,
    Departamento,
    Processo,
    Documento,
    Portaria,
    Pedido,
    Envio,
    Tramite
)
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    pass

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Portaria)
class PortariaAdmin(admin.ModelAdmin):
    pass

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    pass

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    pass

