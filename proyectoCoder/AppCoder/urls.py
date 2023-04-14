from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path("crearCurso/", crearCurso, name="CrearCurso"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="cursos"),
    path("entregables/", entregables, name="entregables"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),
    



]