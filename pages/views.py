from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from pages.models import Movie,Genre

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
        genre_id = request.POST.get('genre')
        genre_obj = get_object_or_404(Genre, id=genre_id)
        title = Movie.objects.create(
            title=request.POST.get('title'),
            rating=int(request.POST.get('rating')),
            genre=genre_obj
        )
        return redirect('home')
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    if request.GET.get('genre'):
        selected_genre = request.GET.get('genre')
        movies = Movie.objects.filter(genre__name=selected_genre)

    context = {
        'movies': movies,
        'genres' : genres,
    }
    return render(request,'home.html',context)
    

def greet(request,name):
    return HttpResponse(f"Hello {name}")

def delete_movie(request,movie_id):
    get_object_or_404(Movie, id=movie_id).delete()
    return redirect('home')

def edit_movie(request,movie_id):
    #fetch
    movie = get_object_or_404(Movie, id=movie_id)
    #if POST
    if request.method == "POST":
        movie.title = request.POST.get('title')
        movie.rating = int(request.POST.get('rating'))
        movie.save()
        return redirect('home')
    #if GET
    else:
        context = {
            'movie': movie,
        }
        return render(request,'edit.html',context)

