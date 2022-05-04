import os
from django.http import HttpResponse
from django.template import Context, Template, loader

def saludo(request):
    return HttpResponse("Bienvenidos!!! Les presento a mis familiares")


def probandoHtml(self):
    
    nom="Fabian"
    ape="Cassarino"
    edad=[58]
    diccionario={'nombre':nom, 'apellido':ape, 'edad':edad}
    
     
    plantilla=loader.get_template("template1.html")
   
  
    documento=plantilla.render(diccionario)
     
    return HttpResponse(documento)
 
     