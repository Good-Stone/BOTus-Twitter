import os

from flask import Flask, Response, jsonify
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)

    # naive CORS setting
    CORS(app)

    load_modules(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def root(path):
        return jsonify(message='Base endpoint. Nothing to do here.')

    return app


# Function for loading the blueprints
def load_modules(app):
    base_URL = '/{}'.format(os.environ.get('VERSION'))
