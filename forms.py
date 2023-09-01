"""Forms for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, validators
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class AddPetForm(FlaskForm):

    pet_name = StringField("Pet Name", validators=[InputRequired()])

    pet_species = StringField("Enter Species",
                              validators=[InputRequired(),
                                            AnyOf(['cat', 'dog', 'porcupine'])])

    pet_photo_url = StringField("Pet Photo Url", validators=[Optional(),
                                                             URL()])

    pet_age = SelectField("Pet Age", choices = [('baby', 'Baby'),
                                                ('young', 'Young'),
                                                 ('adult', 'Adult'),
                                                 ('senior', 'Senior')],
                                                 validators=[InputRequired(),
                                                             AnyOf(['baby',
                                                                    'young',
                                                                    'adult',
                                                                    'senior'])])

    pet_notes = TextAreaField("Notes About The Pet", validators=[Optional()])