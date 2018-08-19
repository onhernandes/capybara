from mongoengine import *

class Photo(Document):
    """Photo's Schema"""
    flickr = StringField(required=True, unique=True)
    tweet = StringField()

