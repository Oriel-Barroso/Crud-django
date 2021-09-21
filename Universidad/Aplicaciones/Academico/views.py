from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages
# Create your views here.

def home(req):
    cursos = Curso.objects.all()
    messages.success(req, 'Cursos listados con exito')
    return render(req, "gestionCursos.html", {"cursos": cursos})


def registrarCurso(req):
    codigo = req.POST['txtCodigo']
    nombre = req.POST['txtNombre']
    creditos = req.POST['numCreditos']
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos
    )
    messages.success(req, 'Curso registrado con exito')
    return redirect('/')


def eliminacionCurso(req, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(req, 'Curso eliminado con exito')
    return redirect('/')


def edicionCurso(req, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(req, "edicionCurso.html", {"curso": curso})


def editarCurso(req):
    codigo = req.POST['txtCodigo']
    nombre = req.POST['txtNombre']
    creditos = req.POST['numCreditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(req, 'Curso actualizado con exito')

    return redirect('/')
