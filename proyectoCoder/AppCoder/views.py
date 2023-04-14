from django.shortcuts import render
from .models import *
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
     if request.method == "POST":
          form = CursoForm(request.POST)
          if form.is_valid():
               nombre= form.cleaned_data['nombre']
               comision = form.cleaned_data['comision']
               curso = Curso()
             
               curso.nombre = nombre
               curso.comision = comision
               curso.save()
               form = CursoForm()
          else:
               pass
     
     else:
          form = CursoForm()

          
     cursos= Curso.objects.all()
     context = {"cursos" : cursos, "form": form}

     return render(request, "AppCoder/cursos.html", context)

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

          
     profesores= Profesor.objects.filter(nombre__icontains="G").all()
     context ={"profesores" : profesores, "form": form}
     return render(request, "AppCoder/profesores.html", context)
   
def estudiantes(request):
     return render(request, "AppCoder/estudiantes.html")
  

def entregables(request):
     if request.method == "POST":
          form = EntregableForm(request.POST)
          if form.is_valid():
               nombre= form.cleaned_data['nombre']
               fecha_entrega = form.cleaned_data['fecha_entrega']
               entregado = form.cleaned_data['entregado']
               entregable= Entregable()
               entregable.nombre = nombre
               entregable.fecha_entrega = fecha_entrega
               entregable.entregado = entregado
               
               entregable.save()
               form = EntregableForm()
          else:
               pass
     
     else:
          form = EntregableForm()

          
     entregable= Entregable.objects.all()
     context ={"entregable" : entregable, "form": form}

     return render(request, "AppCoder/entregables.html", context)
    
def inicioApp(request):
     return render(request, "AppCoder/inicio.html")
    


