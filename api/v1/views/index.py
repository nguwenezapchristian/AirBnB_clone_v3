#!/usr/bin/python3
"""this returns the staus of our api"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """this returns status

    Returns:
        _type_: _description_
    """
    return jsonify({
        "status": "OK"
        })
