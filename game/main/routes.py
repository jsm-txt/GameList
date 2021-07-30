from flask import Blueprint, render_template, request, redirect, url_for,json
from flask.templating import render_template_string
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

@main.route("/about")
def about():
    """Return the about page to the user"""

    return render_template("about.html")

@main.route("/game/<game_title>")
def game_title(game_title):
    """Return the game page to the user"""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "games.json")
    data = json.load(open(json_url))
    for game in data:
        print(game["title"])
        game_data=game
        if game["title"] == game_title:
            break
    print(game_data)

    return render_template("game.html", game_data=game_data)

@main.route("/top_games")
def top_games():
    """Return a game list page to the user"""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "games.json")
    data = json.load(open(json_url))
    

    return render_template("top_games.html", data=data)





