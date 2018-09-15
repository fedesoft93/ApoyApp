from django.contrib import admin
from .models import Entidad, Fundacion, Persona, Evento, Apoyo_Voluntario, Apoyo_Monetario, Apoyo_Menaje
# Register your models here.
admin.site.register(Persona)
admin.site.register(Fundacion)
admin.site.register(Evento)
admin.site.register(Apoyo_Voluntario)
admin.site.register(Apoyo_Monetario)
admin.site.register(Apoyo_Menaje)