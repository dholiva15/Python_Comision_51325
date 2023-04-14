from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from .forms import *

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
     if request.method == "POST":
          form = ProfesorForm(request.POST)
          if form.is_valid():
               nombre= form.cleaned_data['nombre']
               apellido = form.cleaned_data['apellido']
               email = form.cleaned_data['email']
               profesion = form.cleaned_data['profesion']
               profesor= Profesor()
               profesor.nombre = nombre
               profesor.apellido = apellido
               profesor.email = email
               profesor.profesion = profesion
               profesor.save()
               form = ProfesorForm()
          else:
               pass
     
     else:
          form = ProfesorForm()

          
     profesores= Profesor.objects.all
     context ={"profesores" : profesores, "form": form}
     return render(request, "AppCoder/profesores.html", context)
   
def estudiantes(request):
     return render(request, "AppCoder/estudiantes.html")
  

def entregables(request):
     return render(request, "AppCoder/entregables.html")
    
def inicioApp(request):
     return render(request, "AppCoder/inicio.html")
    


