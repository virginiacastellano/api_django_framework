from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset= Programmer.objects.all()
    serializer_class= ProgrammerSerializer
    
# En resumen, este archivo views.py es esencial para configurar cómo se manejarán las solicitudes HTTP relacionadas con los programadores en tu API. Proporciona una vista basada en clases (ProgrammerViewSet) que se encarga de las operaciones CRUD para los programadores utilizando la lógica predefinida de DRF, y especifica cómo se serializarán estos datos antes de ser enviados como respuestas JSON.