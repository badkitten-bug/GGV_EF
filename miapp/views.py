from ast import Return
import xdrlib
from django.shortcuts import render, HttpResponse, redirect
from requests import request
from miapp.models import Producto

# Create your views here.

layout = """

                <h1> TA (LP3) |GGV <h1>
                <hr>


          """


def saludo(request):

    return render(request, 'saludo.html', {
        'titulo': 'saludo',
        'saludo': 'Bienvenidos a la Evidencia '

    })


def integrantes(request):

    estudiantes = ['Gomez Marcos Emily',
                   'Vilca ramirez Alfredo', 
                   'Gomez Huamani steve']
 
    return render(request,'integrantes.html', {
        'titulo':'Inicio',
        'mensaje':'Examen Final LP3 :c',
        'estudiantes': estudiantes
    })


def crear_producto(request):
    
    producto = Producto(
        codigo = "1926040817",
        nombre = "oro",
        precio_compra = "8.5",
        precio_venta = "12",
        Fecha_compra = "2022-04-15",
        Fecha_registro = "2022-08-12",
        estado = "A"
    )
    producto.save()

    return HttpResponse(f"Producto Creado: {producto.codigo} - {producto.nombre} - {producto.precio_compra} - {producto.precio_venta} - {producto.Fecha_compra} - {producto.Fecha_registro} - {producto.estado}")
    