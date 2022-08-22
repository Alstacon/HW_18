from application.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_params(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create(self, data):
        try:
            movie = Movie(**data)

            self.session.add(movie)
            self.session.commit()

            return movie
        except Exception as e:
            print(f"""Ошибка при добавлении фильма {e}""")
            self.session.rollback()

    def update(self, data):
        try:
            self.session.add(data)
            self.session.commit()

            return data
        except Exception as e:
            print(f"""Ошибка при обновлении фильма {e}""")
            self.session.rollback()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
