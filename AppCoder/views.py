from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Usuario creado exitosamente")

