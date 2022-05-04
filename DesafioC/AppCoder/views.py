from django.shortcuts import render
from .models import Familiar1, Familiar2, Familiar3
from django.http import HttpResponse

# Create your views here.

def familiar(self):
    familiar=Familiar1(nombre="Fabian Cassarino", edad=58, email="fabi@gmail.com")
    familiar.save()
    texto= f"nombre: {familiar.nombre} edad: {familiar.edad} email: {familiar.email}"
    return HttpResponse(texto)

def familiar2(self):
    familiar2=Familiar2(nombre="Marisa Guerra", edad=52, email="mary@gmail.com")
    familiar2.save()
    texto= f"nombre: {familiar2.nombre} edad: {familiar2.edad} email: {familiar2.email}"
    return HttpResponse(texto)

def familiar3(self):
    familiar3=Familiar3(nombre="Melina Cassarino", edad=17, email="meli@gmail.com")
    familiar3.save()
    texto= f"nombre: {familiar3.nombre} edad: {familiar3.edad} email: {familiar3.email}"
    return HttpResponse(texto)
