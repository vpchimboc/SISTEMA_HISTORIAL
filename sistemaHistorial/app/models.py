import uuid
from autoslug import AutoSlugField
from django.db import models

# Create your models here.

from datetime import date
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dni = models.CharField('N de documento', max_length=13, unique=True, blank=False, null=False)
    fecha_nacimiento = models.DateField("Fecha de nacimiento", default=date.today, null=False, blank=False)
    telefono = models.CharField('Teléfono', max_length=10, blank=True, null=True)
    celular = models.CharField('Celular', max_length=10, blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=40, blank=True, null=True)
    genero = models.PositiveIntegerField("Género", choices=[(1, "MASCULINO"), (2, "FEMENINO")], default=1)
    tipo = models.PositiveIntegerField("Tipo", choices=[(1, "ENFERMERA/O"), (2, "MÉDICO")], default=1)
   
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'usuario'
        
def generar_slug(instance):
        return '{0}'.format(uuid.uuid4())

class Paciente(models.Model):
    nombre = models.CharField("Nombres", max_length=65, null=False, blank=False)
    apellido = models.CharField("Apellidos", max_length=65, null=False, blank=False)
    dni = models.CharField('N de documento', max_length=10, unique=True, blank=False, null=False)
    fecha_nacimiento = models.DateField("Fecha de nacimiento", default=date.today, null=False, blank=False)
    genero = models.PositiveIntegerField("Género", choices=[(1, "MASCULINO"), (2, "FEMENINO")], default=1)
    email = models.EmailField("Correo electrónico", max_length=45, unique=True, blank=True, null=True)
    telefono = models.CharField("Teléfono", max_length=10, blank=True, null=True)
    celular = models.CharField("Celular", max_length=10, blank=True, null=True)
    direccion = models.CharField("Dirección", max_length=60, null=True, blank=True)
    estado = models.BooleanField("Estado", default=True)
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now=False, auto_now_add=True)
    slug = AutoSlugField(populate_from=generar_slug, editable=False)
       
    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)


    class Meta:
        db_table = 'paciente'


class Ficha_Medica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente", related_name="ficha_medica_paciente")
    fecha = models.DateField("Fecha", default=date.today, null=False, blank=False)
    diagnostico = models.CharField("Diagnostico", max_length=200, blank=False, null=False)
    tratamiento = models.CharField("Tratamiento", max_length=200, blank=False, null=False)
    observacion = models.CharField("Observación", max_length=100, blank=True, null=True)
    alta = models.BooleanField("Dado de alta", default=False)
    estado = models.BooleanField("Estado", default=True)
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now=False, auto_now_add=True)
    slug = AutoSlugField(populate_from=generar_slug, editable=False)

    def __str__(self):
        return '{0} {1} {2}'.format(self.paciente.nombre, self.paciente.apellido, self.paciente.dni)


    class Meta:
        db_table = 'ficha_medica'


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, verbose_name="Paciente", related_name="consulta_paciente")
    fecha = models.DateField("Fecha", default=date.today, null=False, blank=False)
    motivo = models.CharField("Motivo", max_length=200, blank=False, null=False)
    observacion = models.CharField("Observación", max_length=100, blank=True, null=True)
    estado = models.BooleanField("Estado", default=True)
    fecha_registro = models.DateTimeField('Fecha de registro', auto_now=False, auto_now_add=True)
    slug = AutoSlugField(populate_from=generar_slug, editable=False)
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.paciente.nombre, self.paciente.apellido, self.paciente.dni)


    class Meta:
        db_table = 'consulta'