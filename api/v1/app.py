#!/usr/bin/python3
"""This is the Flask module for our API."""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

HBNB_API_HOST = getenv('HBNB_API_HOST')
HBNB_API_PORT = getenv('HBNB_API_PORT')


@app.teardown_appcontext
def close_app(exception):
    """this closes the app

    Args:
        exception (_type_): _description_
    """
    storage.close()


if __name__ == "__main__":
    if HBNB_API_HOST and HBNB_API_PORT:
        app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
    else:
        app.run(host='0.0.0.0', port=5000, threaded=True)
