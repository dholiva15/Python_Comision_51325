from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=50) #estoy diciendo que va a ser un texto con no mas de 50 caracteres
    comision= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()

class Avatar(models.Model):
    imagen= models.ImageField(upload_to = "avatars")
    user= models.ForeignKey(User, on_delete= models.CASCADE)
