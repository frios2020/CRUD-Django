# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import application
  
# create a ModelForm 
class ApplicationForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = application 
        fields = ['ficharegistral','fecharegistro', 'nombres', 'dni', 'tarifa' , 'docs_adjuntos', 'observaciones',]
        labels = {
        "ficharegistral": "Ficha Registral",
        "fecharegistro": "Fecha de Registro",
        "nombres":"Apellidos y Nombres:",
        "dni":"DNI:",
        "tarifa":"Tarifa:",
        "docs_adjuntos":"Documentos adjuntos:",
        "observaciones":"Observaciones:"
        }
        