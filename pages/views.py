from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'username': 'vinu'})

def greet(request,name):
    return HttpResponse(f"Hello {name}")