# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_descripcion = models.CharField(max_length=100,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_area'
        
    def __str__(self):
        return self.area_descripcion


class Modalidad(models.Model):
    modalidad_id = models.AutoField(primary_key=True)
    modalidad_descripcion = models.CharField(max_length=100,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_modalidad'
    
    def __str__(self):
        return self.modalidad_descripcion


class Nivel(models.Model):
    nivel_id = models.AutoField(primary_key=True)
    nivel_descripcion = models.CharField(max_length=100,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_nivel'
        
    def __str__(self):
        return self.nivel_descripcion

class Periodo(models.Model):
    periodo_id = models.AutoField(primary_key=True)
    periodo_descripcion = models.CharField(max_length=100,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_periodo'
        
    def __str__(self):
        return self.periodo_descripcion
        
class TipoContacto(models.Model):
    tipo_contacto_id = models.AutoField(primary_key=True)
    tipo_contacto_descripcion = models.CharField(max_length=255,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_tipo_contacto'
        
    def __str__(self):
        return self.tipo_contacto_descripcion


class TipoEstudio(models.Model):
    tipo_estudio_id = models.AutoField(primary_key=True)
    tipo_estudio_descripcion = models.CharField(max_length=255,verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tbl_tipo_estudio'
        
    def __str__(self):
        return self.tipo_estudio_descripcion


class Ubicacion(models.Model):
    ubicacion_id = models.AutoField(primary_key=True)
    ubicacion_pais = models.CharField(max_length=255,verbose_name='Pais')
    ubicacion_ciudad = models.CharField(max_length=255,verbose_name='Ciudad')
    ubicacion_codigo = models.CharField(max_length=50, blank=True, null=True,verbose_name='Codigo')

    class Meta:
        managed = False
        db_table = 'tbl_ubicacion'
    
    def __str__(self):
        return self.ubicacion_ciudad


class Postulante(models.Model):
    postulante_id = models.AutoField(primary_key=True)
    postulante_nombres = models.CharField(max_length=255)
    postulante_apellidos = models.CharField(max_length=255)
    postulante_nrodocide = models.CharField(max_length=100)
    postulante_fecnac = models.DateField()
    postulante_genero = models.CharField(max_length=1)
    postulante_estado = models.CharField(max_length=1)
    postulante_fecreg = models.DateTimeField()
    postulante_perfil = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_postulante'
        
    def __str__(self):
        return self.postulante_nombres


class Oferta(models.Model):
    oferta_id = models.AutoField(primary_key=True)
    oferta_titulo = models.CharField(max_length=255)
    oferta_fec_pub = models.DateField()
    oferta_fec_fin = models.DateField()
    oferta_resumen = models.TextField(blank=True, null=True)
    oferta_detalle = models.TextField(blank=True, null=True)
    oferta_estado = models.IntegerField()
    oferta_fecreg = models.DateTimeField()
    ubicacion = models.ForeignKey(Ubicacion, models.RESTRICT)
    modalidad = models.ForeignKey(Modalidad, models.RESTRICT)
    area = models.ForeignKey(Area, models.RESTRICT, related_name='Ofertas')
    periodo = models.ForeignKey(Periodo, models.RESTRICT)
    nivel = models.ForeignKey(Nivel, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'tbl_oferta'
        
    def __str__(self):
        return self.oferta_titulo


class OfertaPostulante(models.Model):
    oferta_postulante_id = models.AutoField(primary_key=True)
    oferta_postulante_fecreg = models.DateTimeField()
    oferta_postulante_estado = models.CharField(max_length=1)
    oferta = models.ForeignKey(Oferta, models.RESTRICT)
    postulante = models.ForeignKey(Postulante, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'tbl_oferta_postulante'
        
    def __str__(self):
        return str(self.oferta_postulante_fecreg)



class PostulanteContacto(models.Model):
    postulante_contacto_id = models.AutoField(primary_key=True)
    postulante_contacto_valor = models.CharField(max_length=255)
    postulante_contacto_estado = models.CharField(max_length=1)
    postulante_contacto_fecreg = models.DateTimeField()
    tipo_contacto = models.ForeignKey(TipoContacto, models.RESTRICT)
    postulante = models.ForeignKey(Postulante, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'tbl_postulante_contacto'
        
    def __str__(self):
        return self.postulante_contacto_valor


class PostulanteEstudio(models.Model):
    postulante_estudio_id = models.AutoField(primary_key=True)
    postulante_estudio_titulo = models.CharField(max_length=255)
    postulante_estudio_institucion = models.CharField(max_length=255)
    postulante_estudio_fecini = models.DateField()
    postulante_estudio_fecfin = models.DateField(blank=True, null=True)
    postulante_estudio_estado = models.CharField(max_length=1)
    postulante_estudio_fecreg = models.DateTimeField()
    tipo_estudio = models.ForeignKey(TipoEstudio, models.RESTRICT)
    postulante = models.ForeignKey(Postulante, models.RESTRICT)
    

    class Meta:
        managed = False
        db_table = 'tbl_postulante_estudio'
        
    def __str__(self):
        return self.postulante_estudio_titulo


class PostulanteExperiencia(models.Model):
    postulante_experiencia_id = models.AutoField(primary_key=True)
    postulante_experiencia_puesto = models.CharField(max_length=255)
    postulante_experiencia_empresa = models.CharField(max_length=255)
    postulante_experiencia_detalle = models.TextField()
    postulante_experiencia_fecini = models.DateField()
    postulante_experiencia_fecfin = models.DateField(blank=True, null=True)
    postulante_experiencia_estado = models.CharField(max_length=1)
    postulante_experiencia_fecreg = models.DateTimeField()
    postulante = models.ForeignKey(Postulante, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'tbl_postulante_experiencia'
        
    def __str__(self):
        return self.postulante_experiencia_empresa


