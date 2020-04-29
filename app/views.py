from flask import render_template
from app import app
from .request import get_movies, get_movie, search_movie

# HomePage
@app.route('/')
def index():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template(
        'index.html', 
        title = title, 
        popular = popular_movies,
        upcoming = upcoming_movies,
        now_showing = now_showing_movies)

# Movie details
@app.route('/movie/<int:id>')
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template(
        'movie.html', 
        title = title,
        movie = movie)

# Movie Search
@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movie = search_movie(movie_name_format)
    title = f'Search results for {movie_name}'
    return render_template(
        'search.html',
        title = title,
        movies = searched_movie
    )
