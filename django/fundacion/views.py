from django.shortcuts import render

def principal(request): # El parametro request, ya que con dicho objeto genera la respuesta cuando se haga la peticion
    # alumnos = Alumno.objects.all() # Traigame todos los registros del modelo Alumno. select * from modelo;
    # return render_to_response("principal.html", {'datos':alumnos}) # Cuando se haga la peticion, retornara el html definido en templates de la app, le paso parametros a la plantilla
    return render(request, "principal.html")
