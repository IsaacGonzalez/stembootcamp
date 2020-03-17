from ..models import Direccion
from rest_framework import serializers

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id', 'calle', 'numero', 'colonia', 'ciudad', 'estado', 'pais', 'codigo_postal', 'fecha')

