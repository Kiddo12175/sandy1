from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
def sandy(request):
    return HttpResponse('<h1>hi sandy</h1>')