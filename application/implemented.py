from application.dao.director import DirectorDAO
from application.dao.genre import GenreDAO
from application.dao.movie import MovieDAO
from application.service.director import DirectorService
from application.service.genre import GenreService
from application.service.movie import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)