from mailbox import NoSuchMailboxError
from unittest import loader
from django.template import Template, Context
from django.template import loader
from django.http import HttpResponse
import datetime

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido

def saludo(request):

    p1=Persona("Damian", "Ramos")
    temascurso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ahora = datetime.datetime.now()

    doc_externo = loader.get_template ("miplantilla.html") #no me toma el get template :(

    documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "horario":ahora, "temas":temascurso}) 
    #De esta manera se muestra en pantalla usando la plantilla HTML, sin usar contexto y cargado a la "web"

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Si ves esto salio bien el primero y el segundo")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    tiempo = """<html>
    <body>
    <h2> 
    Fecha y Hora exacta %s 
    </html>
    </body>
    </h2>""" % fecha_actual

    return HttpResponse(tiempo)

def CalculoDeEdad(request, edad, agno):
   
    periodo = agno-2022
    edadfutura= edad + periodo
    documento = "<html><body><h2> En el año %s tendras %s años" %(agno, edadfutura)

    return HttpResponse(documento)