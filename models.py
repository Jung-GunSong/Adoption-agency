"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ creates instances of pets"""
    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
    )

    species = db.Column(
        db.String(50),
        nullable=False,
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    age = db.Column(
        db.Text,
        nullable=False,
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
