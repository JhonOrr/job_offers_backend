from rest_framework import serializers
from .models import Postulante, Area, Modalidad, Nivel, Periodo,  TipoContacto, TipoEstudio, Oferta

#Vistas generales
class ModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "modalidad_id",
            "modalidad_descripcion"
        )
        model = Modalidad

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Area

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "nivel_id",
            "nivel_descripcion"
        )
        model = Nivel

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "periodo_id",
            "periodo_descripcion"
        )
        model = Periodo

class TipoContactoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "tipo_contacto_id",
            "tipo_contacto_descripcion"
        )
        model = TipoContacto

class TipoEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "tipo_estudio_id",
            "tipo_estudio_descripcion"
        )
        model = TipoEstudio

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  
        model = Postulante

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Oferta
    
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation


class AreaOfertaSerializer(serializers.ModelSerializer):
    Ofertas = OfertaSerializer(many=True,read_only=True)
    class Meta:
        model = Area
        fields = ["area_id","area_descripcion", "Ofertas"] 
        

