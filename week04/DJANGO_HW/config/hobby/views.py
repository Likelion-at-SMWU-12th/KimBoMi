from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myhobby(request):
    return render(request, 'hobby.html')