from src.models import Movie
from src.models import db
class MovieRepository:

    def get_all_movies(self):
        
        return Movie.query.all()
   

    def get_movie_by_id(self, movie_id):
        return Movie.query.filter_by(Movie.movie_id(movie_id)).all()

    def create_movie(self, titl, dir, rat):
        new_movie= Movie(title = titl, director=dir, rating=rat)
        db.session.add(new_movie)
        db.session.commit()
        return None

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        Movie.query.filter_by(Movie.title == title)
        return 


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
