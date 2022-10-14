from django.db import models
from datetime import datetime, date

# Create your models here.

class Articulo(models.Model):

    def __str__(self):
        return f"Artículo: {self.nombre} - {self.animal}"

    nombre = models.CharField(max_length=60)
    animal = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField() 
    fecha = models.DateField(auto_now_add=True)


class Review(models.Model):

    comentario = models.CharField(max_length=120)
    usuario = models.CharField(max_length=30)


