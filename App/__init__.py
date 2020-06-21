from flask import Flask

from App.apis import init_api
from App.middleware import load_middleware
from App.settings import envs
from App.ext import init_ext


def create_app(env):
    app = Flask(__name__)

    # 加载项目配置
    app.config.from_object(envs.get(env))

    # 加载第三方插件
    init_ext(app)

    # 加载api
    init_api(app)

    # 加载中间件
    load_middleware(app)

    return app