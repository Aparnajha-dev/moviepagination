from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Movies


def movie_list(request):
    movies = Movies.objects.all().order_by('id')

    paginator = Paginator(movies, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/movie_list.html', {
        'page_obj': page_obj
    })

