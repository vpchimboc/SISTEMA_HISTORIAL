from django.contrib import admin
from app.models import User,Paciente,Ficha_Medica,Consulta
# Register your models here.

admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Ficha_Medica)
admin.site.register(Consulta)