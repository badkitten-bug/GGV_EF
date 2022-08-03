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
