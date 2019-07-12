from flask import Flask
from flask_caching import Cache
from flask_restful import Api

from .config import Config

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
cache = Cache(app)
