from . import app_views
from flask import Flask, jsonify


j_dict = {
          "status": "OK"
          }


@app_views.route('/status')
def status():
    """returns status"""
    return (jsonify(j_dict))
