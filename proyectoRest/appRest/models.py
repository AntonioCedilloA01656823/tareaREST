from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.IntegerField()
    password = models.CharField(max_length= 10)

class Partidas(models.Model):
    id = models.IntegerField()
    fecha = models.CharField(max_length=8)
    id_usuario = models.CharField(max_length=3)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

