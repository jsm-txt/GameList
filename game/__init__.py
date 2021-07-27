
from flask import Flask
from game.config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config.from_object(Config)

app.config["MONGO_URI"] = "mongodb://localhost:27017/gamelist"

mongo = PyMongo(app)
db = mongo.db

from game.main.routes import main

app.register_blueprint(main)