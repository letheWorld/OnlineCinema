from flask import request, g, current_app


def load_middleware(app):

    @app.before_request
    def before():

        print('中间件', request.url)


    @app.after_request
    def after(response):

        return response