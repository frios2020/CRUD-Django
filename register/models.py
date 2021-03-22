from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class application(models.Model):
    ficharegistral = models.CharField(max_length=12)
    fecharegistro = models.DateField()
    nombres = models.CharField(max_length=120)
    dni = models.IntegerField()
    tarifa = models.ForeignKey('tarifa',on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    docs_adjuntos = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=150)
    fecharecepcion = models.DateField(blank=True, null=True)
    hojaremision = models.CharField(max_length=16, blank=True)
    fechaentrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, choices=[
        ('R',"Registrado"),
        ('E',"Enviado"),
        ('O',"Recibido"),
        ('X',"Entregado")
    ])

    def __str__(self):
        return self.ficharegistral + "-"+self.nombres

class tarifa(models.Model):
    codigo = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.codigo + "-"+self.descripcion