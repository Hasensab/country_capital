from django.shortcuts import render
from app.models import *

# Create your views here.
def display_country(request):
    CTO=Country.objects.all()
    d={'country':CTO}
    return render(request,'country.html',d)
