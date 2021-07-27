from flask import Blueprint, render_template, request, redirect, url_for
from game import db
from bson.objectid import ObjectId
import random
import requests
import os


main = Blueprint("main", __name__)


@main.route("/")
def landingPage():
    """Return our landing page to the user."""
    return render_template("home.html")


