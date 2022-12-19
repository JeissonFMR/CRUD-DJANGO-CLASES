from operator import mod
from pyexpat import model
from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models
from .clientes import *
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
# Create your models here.


   
class TipoProceso(models.Model):
    nombre = models.CharField(max_length=150, null=True, verbose_name='Tipo proceso')

    def __str__(self):
        fila =  self.nombre
        return fila
    
class Programa(models.Model):  
    nombre_programa = models.CharField(max_length=150, null=True, verbose_name='Nombre del programa')
    def __str__(self):
        fila = "nombre programa: " + self.nombre_programa
        return fila



class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    
    programa = models.ForeignKey(Programa,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Nombre del programa')
    def __str__(self):
        fila = "nombre: " + self.nombre + " - " + "programa: " + str(self.programa)
        return fila


class Country(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Procesos(models.Model):
    # id = models.AutoField(primary_key=True)
    idp_pro = models.CharField(max_length=10, verbose_name='Identificación', unique=True)
    nom_pro = models.CharField(max_length=150, null=True, verbose_name='Nombre')
    cli_pro = models.CharField(max_length=1, choices=cliente, default='E', verbose_name='Cliente')
    pre_pro = models.CharField(max_length=150, verbose_name='Preguntas')
    res_pro = models.CharField(max_length=150, verbose_name='Respuestas')
    pla_pro = models.CharField(max_length=100, choices=plataforma, default='Ruha', verbose_name='Plataforma')
    
    doc_pro = models.CharField(max_length=2, choices=suceptible_automatizar, default='No',verbose_name='Documentos')
    rep_pro = models.CharField(max_length=150, verbose_name='Responsable')
    tie_pro = models.CharField(max_length=100, choices=horas_proceso, default='1-4 horas', verbose_name='Tiempo de respuesta del proceso')

    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE, null=True, related_name='Procesos')
    aut_pro = models.CharField(max_length=2, choices=suceptible_automatizar, default='No',verbose_name='Automatizar')

    day  = datetime.datetime.now()
    formatedDay  = day.strftime("%Y/%m/%d")
    formatedHora = day.strftime("%H:%M:%S")
    fec_pro = models.CharField(max_length=50, editable=False, default=formatedDay, verbose_name='Fecha')
    hor_pro = models.CharField(max_length=50, editable=False, default=formatedHora, verbose_name='Hora')

    tipoprocesoid = models.ForeignKey(TipoProceso,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Tipo proceso')
    programaid = models.ForeignKey(Programa,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Nombre del programa')
    responsableid = models.ForeignKey(Responsable,null=True, blank=True, on_delete=models.PROTECT, verbose_name='Responsbale')
    
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey('City', null=True, blank=True, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse("procesos")
    
    def __str__(self):
        fila = "Identificación: " + self.idp_pro + " - " + "Nombre: " + self.pre_pro
        return fila
    

