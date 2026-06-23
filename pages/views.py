from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Movie

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'username': 'vinu'})

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request,'home.html',context)

def greet(request,name):
    return HttpResponse(f"Hello {name}")