from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from pages.models import Movie

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'username': 'vinu'})

# def home(request):
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request,'home.html',context)

def home(request):
    if request.method == "POST":
        title = Movie.objects.create(title=request.POST.get('title'),rating=int(request.POST.get('rating')))
        # Post/Redirect/Get
        return redirect('home')
        
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request,'home.html',context)
    

def greet(request,name):
    return HttpResponse(f"Hello {name}")

def delete_movie(request,movie_id):
    get_object_or_404(Movie, id=movie_id).delete()
    return redirect('home')

def edit_movie(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        movie.title = request.POST.get('title')
        movie.rating = int(request.POST.get('rating'))
        movie.save()
        return redirect('home')
    else:
        context = {
            'movie': movie,
        }
        return render(request,'edit.html',context)

