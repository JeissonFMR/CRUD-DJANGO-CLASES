from distutils.text_file import TextFile
from logging import PlaceHolder
from selectors import SelectSelector
#from tkinter import Widget
#from attr import attr
from django.forms import TextInput, TimeInput, ModelForm, RadioSelect, HiddenInput

from .models import Procesos

class ProcesosFormulario(ModelForm):
    class Meta:
        model = Procesos
        fields = '__all__'
        widgets = {
            #PREGUNTAR PORQUE NO FUNCIONA EL PLACEHOLDER
            'idp_pro':TextInput(attrs={'type': 'text','class' : 'identifiacaion_proceso', 'placeholder':'Identificación del proceso', 'required' : 'required', 'pattern' : '[A-Za-z0-9]+'}),
            
            'nom_pro':TextInput(attrs={'type': 'text','class' : 'nombre_proceso', 'placeholder':'Nombre del proceso', 'pattern' : '[A-Za-z]+', 'required' : 'required' }),

            'pre_pro':TextInput(attrs={'type': 'text','class' : 'pregunta_proceso', 'placeholder':'Pregunta del proceso', 'required' : 'required' }),
            
            'res_pro':TextInput(attrs={'type': 'text','class' : 'respuesta_proceso', 'placeholder':'Respuesta del proceso', 'required' : 'required' }),

            'aut_pro':RadioSelect(attrs={'type': 'radio','class' : 'automatizacion_proceso',  }),

            'fec_pro':TimeInput(attrs={'type': 'month','class' : 'fech_creacion_proceso', 'placeholder':'Creacion del proceso', 'required' : 'required' }),

            'hor_pro':TimeInput(attrs={'type': 'time','class' : 'hor_creacion_proceso', 'placeholder':'Creacion Hora del proceso', 'required' : 'required' }),

        }

