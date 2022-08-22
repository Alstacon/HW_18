from flask import request, url_for
from flask_restx import Resource, Namespace

from application.dao.model.movie import MovieSchema
from application.implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if request.args:
            return movies_schema.dump((movie_service.get_by_params(request.args))), 200

        return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        req_json = request.json
        if movie_service.create(req_json):

            return '', 201, {'Location': url_for('movies_movies_view')}
        else:
            return '', 503


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)

        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json

        movie_service.update(req_json)

        return '', 204

    def patch(self, mid):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)

        return '', 204
