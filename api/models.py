# models.py: Definición de Modelos de Datos

# En este archivo, definimos los modelos de datos que nuestra API utilizará. Los modelos representan
# las estructuras de datos de nuestra aplicación y cómo se almacenan en la base de datos.

# Importamos la clase `models` de Django, que nos permite definir modelos de datos.
from django.db import models

# Creamos una clase llamada `Programmer` que hereda de `models.Model`. Esto define un modelo de datos
# llamado 'Programmer' que se traducirá en una tabla en nuestra base de datos.

class Programmer(models.Model):
    # Definimos los campos de nuestro modelo. En este caso, tenemos los siguientes campos:
    
    fullname = models.CharField(max_length=100)  # Un campo para el nombre completo del programador.
    nickname = models.CharField(max_length=50)   # Un campo para el apodo o alias del programador.
    age = models.PositiveSmallIntegerField()     # Un campo para la edad del programador.
    isaxtive = models.BooleanField(default=True)  # Un campo booleano que indica si el programador está activo o no.

# Estos campos representan la estructura de nuestros programadores en la base de datos.
