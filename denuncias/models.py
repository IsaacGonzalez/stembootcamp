from django.db import models
"""
Denuncia 
 - fecha 
 - direccion 
 - usuario
 - descripcion

Direccion
 - calle
 - numero 
 - colonia
 - ciudad
 - estado
 - pais
 - codigo postal
"""
class Direccion(models.Model):

    calle = models.CharField(max_length=200)
    numero = models.IntegerField()
    colonia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    codigo_postal = models.IntegerField()
    fecha = models.DateTimeField('date published')

    def __str__(self):
        return self.calle + ", " + self.colonia + " " + self.ciudad