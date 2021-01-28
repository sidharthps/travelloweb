from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'The city never sleeps'
    dest1.price = 700
    dest1.image = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Chennai'
    dest2.description = 'Developing City'
    dest2.price = 900
    dest2.image = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Hyderabad'
    dest3.description = 'Ramoji Rao Film City'
    dest3.price = 1000
    dest3.image = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1,dest2,dest3]


    return render(request,"index.html",{'dests':dests})