from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crearCurso (request):
    nombre_curso= "Python"
    comision_curso= 51325

    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta = f"Curso creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)


def cursos (request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
     return render(request, "AppCoder/profesores.html")
   
def estudiantes(request):
     return render(request, "AppCoder/estudiantes.html")
  

def entregables(request):
     return render(request, "AppCoder/entregables.html")
    
def inicioApp(request):
     return render(request, "AppCoder/inicio.html")
    


