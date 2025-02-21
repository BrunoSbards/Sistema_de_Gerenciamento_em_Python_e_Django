from django.db import models
from django.contrib.auth.models import User


class estado(models.Model):    
    sigla_estado = models.CharField(max_length=5)

    def __str__(self):
        return self.sigla_estado


class leiloeiro(models.Model):      
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    site = models.URLField()
    
    def __str__(self):
        return self.nome
    

class matricula(models.Model):    
    id_estado = models.ForeignKey(estado, on_delete=models.CASCADE)
    id_leiloeiro = models.ForeignKey(leiloeiro, on_delete=models.CASCADE)
    numero_matricula = models.CharField(max_length=10)
    
    def __str__(self):
        return self.numero_matricula
    

class anexo(models.Model):
    id_leiloeiro = models.ForeignKey(leiloeiro, on_delete=models.CASCADE, null=True, blank=True)
    arquivo = models.CharField(max_length=255)

    def __str__(self):
        return self.arquivo
