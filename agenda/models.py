from django.db import models
from clientes.models import Cliente
from processos.models import Processo

class Compromisso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField()
    local = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.data.strftime('%d/%m/%Y %H:%M')}"
