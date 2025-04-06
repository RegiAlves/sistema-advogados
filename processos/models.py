from django.db import models
from clientes.models import Cliente

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    vara = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=20)
    data_abertura = models.DateField()

    def __str__(self):
        return f"Processo {self.numero} - {self.cliente.nome}"
    
class Compromisso(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name='compromissos_processos'  # NOME ÚNICO
    )
    processo = models.ForeignKey(
        Processo, 
        on_delete=models.CASCADE, 
        related_name='compromissos_processos'  # NOME ÚNICO
    )
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField()
    local = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.titulo} - {self.data.strftime('%d/%m/%Y %H:%M')}"
