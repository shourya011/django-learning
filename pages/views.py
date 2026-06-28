from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from pages.models import Movie,Genre
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def home(request):
#     return render(request,'home.html',{'username': 'vinu'})

# def home(request):
    # movies = Movie.objects.all()
    # context = {
    #     'movies': movies,
    # }
    # return render(request,'home.html',context)
@login_required
def home(request):
    if request.method == "POST":
        title_value = request.POST.get('title')
        rating_value = request.POST.get('rating')
        genre_id = request.POST.get('genre')
        genre_obj = get_object_or_404(Genre, id=genre_id)
        if title_value and rating_value:
            Movie.objects.create(
                title=title_value,
                rating=int(rating_value),
                genre=genre_obj,
                user=request.user
            )
            messages.success(request, "Movie added!")
            return redirect('home')
        else:
            messages.error(request, "Title and rating are required.")
            return redirect('home')

    genres = Genre.objects.all()
    movies = Movie.objects.filter(user=request.user)
    if request.GET.get('genre'):
        selected_genre = request.GET.get('genre')
        movies = movies.filter(genre__name=selected_genre)

    if request.GET.get('q'):
        movie_name = request.GET.get('q')
        movies = movies.filter(title__icontains=movie_name)

    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'home.html', context)
    

def greet(request,name):
    return HttpResponse(f"Hello {name}")

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, user=request.user)
    movie.delete()
    return redirect('home')

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, user=request.user)
    if request.method == "POST":
        movie.title = request.POST.get('title')
        movie.rating = int(request.POST.get('rating'))
        movie.save()
        return redirect('home')
    else:
        context = {
            'movie': movie,
        }
        return render(request, 'edit.html', context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
