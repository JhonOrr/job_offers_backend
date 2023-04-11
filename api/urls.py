from django.urls import path
from .views import (ModalidadListView,AreaListView, NivelListView, PeriodoListView, TipoContactoView, 
                    TipoEstudioView, PostulanteView, OfertaView, ModalidadDetailView, AreaDetailView,
                    NivelDetailView, PeriodoDetailView, TipoContactoDetailView, TipoEstudioDetailView,
                    PostulanteDetailView, OfertaDetailView, AreaOfertaView)
urlpatterns = [
    path("modalidad", ModalidadListView.as_view()),
    path("area", AreaListView.as_view()),
    path("nivel", NivelListView.as_view()),
    path("periodo", PeriodoListView.as_view()),
    path("tipocontacto", TipoContactoView.as_view()),
    path("tipoestudio", TipoEstudioView.as_view()),
    path("postulante", PostulanteView.as_view()),
    path("ofertas", OfertaView.as_view()),
    path("modalidad/<int:pk>", ModalidadDetailView.as_view()),
    path("area/<int:pk>", AreaDetailView.as_view()),
    path("nivel/<int:pk>", NivelDetailView.as_view()),
    path("periodo/<int:pk>", PeriodoDetailView.as_view()),
    path("tipocontacto/<int:pk>", TipoContactoDetailView.as_view()),
    path("tipoestudio/<int:pk>", TipoEstudioDetailView.as_view()),
    path("postulante/<int:pk>", PostulanteDetailView.as_view()),
    path("ofertas/<int:pk>", OfertaDetailView.as_view()),
    path("area/<int:pk>/ofertas", AreaOfertaView.as_view()),
]