from django.db import models

# Create your models here.
class Destination:
    id : int
    name: str
    image : str
    destination : str
    price : int
    offer : bool
