from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path("crearCurso/", crearCurso, name="CrearCurso"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
    path("entregables/", entregables, name="entregables"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),
    path("login/", login_request, name= "login"),
    path("register/", register, name= "register"),
    path('logout/', LogoutView.as_view(template_name = "AppCoder/logout.html"), name='logout'),
   
   
    

]