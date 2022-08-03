from ast import Return
import xdrlib
from django.shortcuts import render, HttpResponse
from requests import request
from miapp.models import Estudiante

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

   


def crear_estudiante(request):
    estudiante = Estudiante(
        codigo="1813011641",
        dni="72721675",
        nombre="emiliano",
        apepat="Sanchez",
        apemat="Maldonado",
        direccion="Mz b lote 10 -PuntaHermosa",
        telefono="958236731",
        estado="A",
    )
    estudiante.save()
    return HttpResponse(f"<h1>Estudiantes Registrados</h1>" +
                        f"<br> <b>Codigo:</b> {estudiante.codigo} <br> <b>DNI:</b> {estudiante.dni} <br> <b>Nombre:</b> {estudiante.nombre}" +
                        f"<br> <b>ApellidoPaterno:</b> {estudiante.apepat} <br> <b>ApellidoMaterno:</b> {estudiante.apemat} <br> <b>Direccion:</b> {estudiante.direccion}" +
                        f"<br> <b>Telefono:</b> {estudiante.telefono} <br> <b>Estado:</b> {estudiante.estado}")

def crearcurso(request):
        return render(request, 'crear-curso.html', {
            'titulo': 'Crear Curso'
        })

def crearproducto(request):
        return render(request, 'crear-producto.html', {
            'titulo': 'Crear Productos'
        })
