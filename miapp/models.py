from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.TextField(max_length=10)
    nombre = models.TextField()
    precio_compra = models.TextField()
    precio_venta = models.TextField()
    Fecha_compra = models.DateField()
    Fecha_registro = models.DateTimeField()
    estado = models.TextField()

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.TextField()
    horas = models.CharField(max_length=100)
    creditos = models.CharField(max_length=100)
    Fecha_registro = models.DateTimeField()
    estado = models.TextField()

