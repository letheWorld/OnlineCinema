from flask_restful import Api

from App.apis.admin.admin_user_api import AdminUsersResource
from App.apis.admin.cinema_auth_api import AdminCinemaResource, AdminCinemasResource

admin_api = Api(prefix='/admin')

admin_api.add_resource(AdminUsersResource, '/adminusers/')

admin_api.add_resource(AdminCinemasResource, '/cinemausers/')
admin_api.add_resource(AdminCinemaResource, '/cinemausers/<int:id>/')