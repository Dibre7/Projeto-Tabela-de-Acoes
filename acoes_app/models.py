import django

from django.db import models

class Acao(models.Model):
    codigo = models.IntegerField()  # Coluna "Código" como inteiro
    acao = models.CharField(max_length=5)  # Coluna "Ação" como texto (máx. 100 caracteres)
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Coluna "Preço" como decimal (ex: 123.45)

    def __str__(self):
        return f"{self.acao} - {self.preco}"
