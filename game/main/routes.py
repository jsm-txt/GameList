from flask import Blueprint, render_template, request, redirect, url_for,json
from game import db
from bson.objectid import ObjectId
import random
import requests
import os


main = Blueprint("main", __name__)


@main.route("/")
def landingPage():
    """Return our landing page to the user."""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "games.json")
    data = json.load(open(json_url))
    print(data)
   

    return render_template("home.html", data=data)

@main.route("/")
def about():
    """Return the about page to the user"""


