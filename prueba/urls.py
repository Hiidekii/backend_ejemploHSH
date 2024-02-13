from django.urls import path
from prueba.views import * #importa todos

urlpatterns = [ #urls de la app prueba
    path("hola", pruebaEndpoint),
    path("nuevo", nuevoEndpoint)
]