from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies' : [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1969
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'year': 1968
        },
        {
            'id': 7,
            'title': 'The Ofiice',
            'year': 1999
        }
        ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")