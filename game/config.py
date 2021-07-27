import os


class Config(object):
    DEBUG = True

    MONGO_URI = os.getenv("MONGO_URI")
