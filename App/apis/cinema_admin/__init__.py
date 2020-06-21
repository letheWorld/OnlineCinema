from flask_restful import Api

from App.apis.cinema_admin.cinema_address_api import CinemaAddressesResource, CinemaAddressResource
from App.apis.cinema_admin.cinema_hall_api import CinemaHallsResource
from App.apis.cinema_admin.cinema_hall_movie_api import CinemaHallMoviesResource
from App.apis.cinema_admin.cinema_movie_api import CinemaMovieResource
from App.apis.cinema_admin.cinema_user_api import CinemaUsersResource

cinema_client_api = Api(prefix='/cinema')

cinema_client_api.add_resource(CinemaUsersResource, '/users/')

cinema_client_api.add_resource(CinemaAddressesResource, '/addresses/')
cinema_client_api.add_resource(CinemaAddressResource, '/addresses/<int:id>/')

cinema_client_api.add_resource(CinemaMovieResource, '/cinemamovies/')

cinema_client_api.add_resource(CinemaHallsResource, '/cinemahalls/')

cinema_client_api.add_resource(CinemaHallMoviesResource, '/cinemahallmovies/')
