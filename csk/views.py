from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Ruturaj is captain of csk</h1>')


def vicecaptain(request):
    return HttpResponse('<h1>Jadeja is  vice captain of csk</h1>')