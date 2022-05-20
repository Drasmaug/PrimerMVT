from django.template import Template, Context
from django.http import HttpResponse
import datetime

def saludo(request):
    
    doc_externo=open("C:/Users/Usuario/Desktop/ProyectosDjango/DjangoProyecto1/DjangoProyecto1/Plantilla1.html")
    
    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx= Context()

    documento = plt.render(ctx)

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