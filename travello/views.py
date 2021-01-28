from django.shortcuts import render
from . models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.description = 'The city never sleeps'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Chennai'
    dest2.description = 'Developing City'
    dest2.price = 900

    dest3 = Destination()
    dest3.name = 'Hyderabad'
    dest3.description = 'Ramoji Rao Film City'
    dest3.price = 1000


    return render(request,"index.html",{'dest1':dest1,
                                        'dest2':dest2,
                                        'dest3':dest3})