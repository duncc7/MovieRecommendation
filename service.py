import requests
from secrets import *

url = "https://api.themoviedb.org/3/"

def getMovieGenres():
    newurl = url + "genre/movie/list?api_key=" + secret() + "&language=en-US"
    genres = requests.get(newurl).json()

    """
    genres returns a JSON object with all the genres, formatted like this:

    {‘genres': 
        [
            {‘id': 28, ‘name': ‘Action'}, 
            {‘id': 12, ‘name': ‘Adventure'},
            ...
            {‘id': 37, ‘name': ‘Western'}
        ]
    }

    Create a new list called "genresList" with only the names, so it's ["Action", "Adventure", ..., "Western"] and return the new list
    """

    # return genresList


def getTVGenres():
    newurl = url + "genre/tv/list?api_key=" + secret() + "&language=en-US"
    genres = requests.get(newurl).json()

    """
    genres returns a JSON object with all the genres, formatted like this:

    {"genres": 
        [
            {"id": 10759, "name": "Action & Adventure"},
            {"id": 16, "name": "Animation"},
            ...
            {"id": 37, "name": "Western"}
        ]
    }

    Create a new list called "genresList" with only the names, so it's ["Action", "Adventure", ..., "Western"] and return the new list
    """

    # return genresList