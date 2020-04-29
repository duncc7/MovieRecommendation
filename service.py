import requests
from secrets import *

url = "https://api.themoviedb.org/3/"

def getMovieGenres():
    newurl = url + "genre/movie/list?api_key=" + secret() + "&language=en-US"
    genres = requests.get(newurl).json()

    """
    genres returns a JSON object with all the genres, formatted like this:

    {'genres': 
        [
            {'id': 28, 'name': 'Action'},
            {'id': 12, 'name': 'Adventure'},
            ...
            {'id': 37, 'name': 'Western'}
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


def getMovieRecs():
    """
    Discover movies api
    https://api.themoviedb.org/3/discover/movie?api_key=" + "&language=en-US"

    - Sort by popularity?

    All optional queries
    - Release Date
    - Popularity
    - Vote Average
    - Genre
    - Runtime (range)

    Get movie IDs
    """

    """
    Use get details api to get movie data?
    https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
    """

    """
    Movie object
    - Title
    - Description
    - Runtime
    - Rating / 10
    - Poster URL (https://image.tmdb.org/t/p/w500/)
    """
    movieList = []
    return movieList