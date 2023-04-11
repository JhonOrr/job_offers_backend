from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Area)
admin.site.register(Modalidad)
admin.site.register(Nivel)
admin.site.register(Periodo)

admin.site.register(TipoContacto)
admin.site.register(TipoEstudio)
admin.site.register(Postulante)
admin.site.register(Oferta)
admin.site.register(OfertaPostulante)
admin.site.register(PostulanteContacto)
admin.site.register(PostulanteEstudio)
admin.site.register(PostulanteExperiencia)

@admin.register(Ubicacion)
class PlatoAdmin(admin.ModelAdmin):

    list_display = ('ubicacion_codigo','ubicacion_pais','ubicacion_ciudad')
    list_filter = ('ubicacion_pais',)