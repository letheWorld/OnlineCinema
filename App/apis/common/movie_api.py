from flask_restful import Resource, reqparse, abort, marshal, fields, marshal_with
from werkzeug.datastructures import FileStorage

from App.apis.admin.utils import login_required
from App.apis.api_constant import HTTP_CREATE_OK, HTTP_OK
from App.apis.common.utils import filename_transfer
from App.models.common.movie_model import Movie

parse = reqparse.RequestParser()
'''
    showname = db.Column(db.String(64))
    shownameen = db.Column(db.String(128))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(32))
    duration = db.Column(db.Integer, default=90)
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.DateTime)
    backgroundpicture = db.Column(db.String(256))
'''
parse.add_argument('showname', required=True, help='must supply showname')
parse.add_argument('shownameen', required=True, help='must supply shownameen')
parse.add_argument('director', required=True, help='must supply director')
parse.add_argument('leadingRole', required=True, help='must supply leadingRole')
parse.add_argument('type', required=True, help='must supply type')
parse.add_argument('country', required=True, help='must supply country')
parse.add_argument('language', required=True, help='must supply language')
parse.add_argument('duration', required=True, help='must supply duration')
parse.add_argument('screeningmodel', required=True, help='must supply screeningmodel')
parse.add_argument('openday', required=True, help='must supply openday')
parse.add_argument('backgroundpicture', type=FileStorage, required=True, help='must supply backgroundpicture', location=['files'])

movie_fields = {
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday': fields.DateTime,
    'backgroundpicture': fields.String,
}

multi_movie_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(movie_fields))
}

class MoviesResource(Resource):

    @marshal_with(multi_movie_fields)
    def get(self):

        movies = Movie.query.all()

        data = {
            'msg': 'OK',
            'status': HTTP_OK,
            'data': movies
        }

        return data

    @login_required
    def post(self):

        args = parse.parse_args()
        showname = args.get('showname')
        shownameen = args.get('shownameen')
        director = args.get('director')
        leadingRole = args.get('leadingRole')
        movie_type = args.get('type')
        country = args.get('country')
        language = args.get('language')
        duration = args.get('duration')
        screeningmodel = args.get('screeningmodel')
        openday = args.get('openday')
        backgroundpicture = args.get('backgroundpicture')

        # backgroundpicture = request.files.get('backgroundpicture')

        movie = Movie()
        movie.showname = showname
        movie.shownameen = shownameen
        movie.director = director
        movie.leadingRole = leadingRole
        movie.type = movie_type
        movie.country = country
        movie.language = language
        movie.duration = duration
        movie.screeningmodel = screeningmodel
        movie.openday = openday

        file_info = filename_transfer(backgroundpicture.filename)
        filepath = file_info[0]
        backgroundpicture.save(filepath)
        movie.backgroundpicture = file_info[1]

        if not movie.save():
            abort(400, msg="can't create movie")

        data = {
            'msg': 'create success',
            'status': HTTP_CREATE_OK,
            'data': marshal(movie, movie_fields)
        }

        return data

class MovieResource(Resource):

    def get(self, id):

        movie = Movie.query.get(id)

        if not movie:
            abort(404, msg='movie is not exist')

        data = {
            'msg': 'OK',
            'status': HTTP_OK,
            'data': marshal(movie, movie_fields)
        }

        return data

    @login_required
    def patch(self, id):
        return {'msg': 'post OK'}

    @login_required
    def put(self, id):
        return {'msg': 'post OK'}

    @login_required
    def delete(self, id):
        return {'msg': 'post OK'}