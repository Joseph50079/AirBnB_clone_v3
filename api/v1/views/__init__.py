#!/usr/bin/python3

"""
app.py module for creating Blueprint
"""

from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__)
