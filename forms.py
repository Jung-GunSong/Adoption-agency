"""Forms for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, validators
from wtforms.validators import InputRequired, Optional, AnyOf, URL

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class PetForm(FlaskForm):
    """creates forms to either add or edit pets"""
    name = StringField("Pet Name", validators=[InputRequired()])

    species = StringField("Enter Species",
                          validators=[InputRequired(),
                                      AnyOf(['CAT', 'DOG', 'PORCUPINE'])])

    photo_url = StringField("Pet Photo Url", validators=[Optional(),
                                                         URL()])

    age = SelectField("Pet Age", choices=[('baby', 'Baby'),
                                          ('young', 'Young'),
                                          ('adult', 'Adult'),
                                          ('senior', 'Senior')],
                      validators=[InputRequired(),
                                  AnyOf(['baby',
                                         'young',
                                         'adult',
                                         'senior'])])

    notes = TextAreaField("Notes About The Pet", validators=[Optional()])
