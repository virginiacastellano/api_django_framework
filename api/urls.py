from django.urls import path, include
from rest_framework import routers
from api import views

# Creación de un enrutador predeterminado de Django REST Framework
router = routers.DefaultRouter()

# Registro de una vista del conjunto de vistas 'ProgrammerViewSet' en el enrutador
router.register(r'programmers', views.ProgrammerViewSet)

# Definición de las URL de la aplicación
urlpatterns = [
    # Incluye todas las URL generadas por el enrutador en las URL principales de la aplicación
    path('', include(router.urls))
]
#En resumen, este archivo configura las rutas necesarias para exponer las funcionalidades de la API REST que se han definido en las vistas de la aplicación, lo que permite a los clientes (como aplicaciones frontend o móviles) acceder y manipular los datos a través de estas URLs.