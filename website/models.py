#* . means __init__.py, db is from that file
from . import db
from flask_login import UserMixin
#*this is to use the func function to generate time
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #!user is lowercase, relationship to User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    #* unique = true means that no other users can have the same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    #!Note is uppercase, relationship to Note table
    notes = db.relationship('Note')
