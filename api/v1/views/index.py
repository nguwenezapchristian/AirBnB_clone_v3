#!/usr/bin/python3
"""this returns the staus of our api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """this returns status"""
    return jsonify({
        "status": "OK"
        })
