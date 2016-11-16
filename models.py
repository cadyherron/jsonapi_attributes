from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    birthday = db.Column(db.DateTime)
