from flask import Flask
from flask_restx import Api
from setup_db import db
from application.views.movie import movie_ns
from application.views.genre import genre_ns
from application.views.director import director_ns
from config import Config


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    with app.app_context():
        register_extension(app)
        return app


def register_extension(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()
