from django.shortcuts import render
from django.http import HttpResponse

from .models import Rockets


# Create your views here.

def index(request):
    rockets = Rockets.objects.all()
    return render(request, 'capsules/index.html', {'rockets': rockets})