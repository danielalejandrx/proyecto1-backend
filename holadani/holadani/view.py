import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    doc= "<html><body><h1>hola mundo esta es nuestra primera pagina</h1></body></html>"
    return HttpResponse(doc)

def chao(request):
    return HttpResponse("nos vemos")

def damefecha(request):
    fecha_actual=datetime.datetime.now()

    docu= """
        <html>
            <body>
                <h1>Fecha y Hora actuales %s </h1>
            </body>
        </html>
    """ % fecha_actual
    return HttpResponse(docu)  


def plantilla(request):

    class Persona(object):
        def __init__(self, nombre, apellido): 
            self.nombre = nombre
            self.apellido = apellido 

    doc_externo = open ("C:/Users/danie/Desktop/backecd23/proyecto1/holadani/holadani/plantilla/miplantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    #nombre= "andres"
    #apellido="Perez"

    p1=Persona("pablo", "Martinez")
    fecha_actual = datetime.datetime.now()

    temascurso=["Modelos","visitas","formularios","Despliegues"]

    ctx = Context ({"nombre_persona": p1.nombre , "apellido_persona" : p1.apellido, "fecha": fecha_actual, "temas":[temascurso]})

    pagina = plt.render(ctx)
 
    return HttpResponse(pagina)
    
    