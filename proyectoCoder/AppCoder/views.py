from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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
     context = {"cursos" : cursos, "form": form, "avatar":obtenerAvatar(request)}

     return render(request, "AppCoder/cursos.html", context)

@login_required
def profesores(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()

    profesores = Profesor.objects.all() #Profesor.objects.filter(nombre__icontains="P").all()
    
    
    return render(request, "AppCoder/profesores.html", {"profesores": profesores, "form" : form , "avatar":obtenerAvatar(request)})



@login_required
def eliminarProfesor(request, id):
     profesor = Profesor.objects.get(id=id)
     print(profesor)
     profesor.delete()
     profesores=Profesor.objects.all()
     form= ProfesorForm()
     return render(request,"AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor Eliminado Correctamente", "form": form, "avatar":obtenerAvatar(request)})

@login_required
def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form= ProfesorForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]

            profesor.save()
            profesores=Profesor.objects.all()
            form = ProfesorForm()
            return render(request, "AppCoder/Profesores.html" ,{"profesores":profesores, "mensaje": "Profesor editado correctamente", "form": form, "avatar":obtenerAvatar(request)})
        pass
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html", {"form": formulario, "profesor": profesor, "avatar":obtenerAvatar(request)})


def estudiantes(request):
     return render(request, "AppCoder/estudiantes.html", {"avatar":obtenerAvatar(request)})
  
@login_required
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
     context ={"entregable" : entregable, "form": form, "avatar":obtenerAvatar(request)}

     return render(request, "AppCoder/entregables.html", context)


def inicioApp(request):
     return render(request, "AppCoder/inicio.html", {"avatar":obtenerAvatar(request)})

login_required
def busquedaComision(request):
     

     return render(request, "AppCoder/busquedaComision.html", {"avatar":obtenerAvatar(request)})

def obtenerAvatar(request):
     avatares = Avatar.objects.filter(user=request.user.id)
     if len(avatares) !=0:
          return avatares[0].imagen.url
     else:
          return "media/avatars/avatarpordefecto.png"


@login_required
def buscar(request):
     comision= request.GET["comision"]
     if comision !="":
          cursos = Curso.objects.filter(comision__icontains=comision)
          return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
     else:
          return render(request, "AppCoder/busquedaComision.html", {"mensaje":"ingrese una comision valida"})
    


def login_request(request):
     if request.method == "POST":
          form= AuthenticationForm(request, data = request.POST)
          if form.is_valid():
               info= form.cleaned_data
               usu=info["username"]
               clave=info["password"]
               usuario=authenticate(username=usu, password=clave)

               if usuario is not None:
                    login(request, usuario)
                    return render(request, "AppCoder/inicio.html", {"mensaje" : f"Usuario {usu} logueado correctamente"})
               else: 
                    return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o Contraseña Incorrectos"})
          
          else: 
               return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o Conraseñas Incorrectos"})

     else: 
          form = AuthenticationForm()
          return render(request, "AppCoder/login.html", {"form": form, })



def register(request):
     if request.method == "POST":
          form= RegistroUsuarioForm(request.POST)
          if form.is_valid():
               username= form.cleaned_data.get("username")
               form.save()
               return render(request, "AppCoder/inicio.html", {"mensaje" : f"Usuario {username} creado correctamente"})

          else: 
               return render(request, "AppCoder/register.html", {"form": form, "mensaje": "Error al crear usuario"})
          
     else: 
          form = RegistroUsuarioForm()
          return render(request, "AppCoder/register.html", {"form": form})

@login_required
def editarPerfil(request):

     
     usuario = request.user
     if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]

            usuario.save()
            
            return render(request, "AppCoder/inicio.html" ,{"mensaje": f"Usuario {usuario.username} editado correctamente" , "avatar":obtenerAvatar(request)})
        else:
          return render(request, "AppCoder/editarPerfil.html" , {"form": form,  "nombreusuario" : usuario.username })
     else:
        form= UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form,  "nombreusuario" : usuario.username })


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
