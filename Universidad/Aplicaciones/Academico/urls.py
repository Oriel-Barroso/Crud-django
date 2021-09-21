from django.urls import path 
from .views import home as Home, registrarCurso as Registro, eliminacionCurso as Eliminacion, edicionCurso as Edicion, editarCurso as Editar


urlpatterns = [
    path('', Home),
    path('registrarCurso/', Registro),
    path('eliminacionCurso/<codigo>', Eliminacion),
    path('edicionCurso/<codigo>', Edicion),
    path('editarCurso/', Editar)

    ]