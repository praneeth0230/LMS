from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def leaves(request):
    return HttpResponse("Hello! I am a leave!")
