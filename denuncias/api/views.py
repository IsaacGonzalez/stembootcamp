from ..models import Direccion
from . import serializers

from rest_framework import generics, status
from rest_framework.response import Response

"""
- Create - crear
- Update - editar
- Read - leer
- Delete - eliminar
"""

class DireccionListView(generics.ListAPIView):
    queryset = Direccion.objects.all()
    serializer_class = serializers.DireccionSerializer

class DireccionCreateView(generics.CreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = serializers.DireccionSerializer

    def create(self, request, *args, **kwargs):
        super(DireccionCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message" : "Succesfully created",
                    "result": request.data
        }
        return Response(response)

class DireccionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = serializers.DireccionSerializer

    def retrieve(self, request, *args, **kwargs):
        super(DireccionDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message" : "Succesfully retrieved",
                    "result": data
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(DireccionDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message" : "Succesfully updated",
                    "result": request.data
        }
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(DireccionDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message" : "Succesfully deleted"
        }
        return Response(response)
