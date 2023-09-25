from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Programmer
        fields='__all__'


#En resumen, este archivo permite definir cómo se debe representar un modelo específico (en este caso, "Programmer") en una API REST. Define cómo se deben convertir las instancias de ese modelo en un formato comprensible, como JSON, para que los clientes de la API puedan interactuar fácilmente con los datos del programador.