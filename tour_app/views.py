from django.shortcuts import render
from .models import container
# Create your views here.

def index(request):

    cont = container()
    cont.tourist = 1000
    cont.years = 25
    cont.cottages = 1200
    cont.restaurants = 679
    return render(request,'index.html',{'cont':cont})