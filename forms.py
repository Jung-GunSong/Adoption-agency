"""Forms for adopt app."""

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

class AddPetForm(FlaskForm):

    pet_name = StringField("Pet Name")

    pet_species = StringField("Enter Species")

    pet_photo_url = StringField("Pet Photo Url")

    pet_age = SelectField("Pet Age", choices = [('baby', 'Baby'), ('young', 'Young'),
                                                 ('adult', 'Adult'), ('senior', 'Senior')])

    pet_notes = TextAreaField("Notes About The Pet")