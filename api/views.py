from django.shortcuts import render
from .serializers import (ModalidadSerializer, AreaSerializer, NivelSerializer, PeriodoSerializer, TipoContactoSerializer,
                          TipoEstudioSerializer, PostulanteSerializer, OfertaSerializer, AreaOfertaSerializer)
from rest_framework import generics
from .models import Modalidad, Area, Nivel, Periodo, TipoContacto, TipoEstudio, Postulante, Oferta
# Create your views here.
# Vistas generales

class ModalidadListView(generics.ListCreateAPIView):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer

class AreaListView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class NivelListView(generics.ListCreateAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class PeriodoListView(generics.ListCreateAPIView):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class TipoContactoView(generics.ListCreateAPIView):
    queryset = TipoContacto.objects.all()
    serializer_class = TipoContactoSerializer

class TipoEstudioView(generics.ListCreateAPIView):
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class PostulanteView(generics.ListCreateAPIView):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer

class OfertaView(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

# vistas CRUD

class ModalidadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer

class AreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class NivelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class PeriodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class TipoContactoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoContacto.objects.all()
    serializer_class = TipoContactoSerializer

class TipoEstudioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class PostulanteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer

class OfertaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer

class AreaOfertaView(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaOfertaSerializer



