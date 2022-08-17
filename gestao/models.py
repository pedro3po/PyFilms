from django.db import models

# Create your models here.
class Filmes(models.Model):
    filme = models.CharField(max_length=50)
    finalizado = models.BooleanField('Finalizado')
    resenha = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=3, decimal_places=1, default=0)
