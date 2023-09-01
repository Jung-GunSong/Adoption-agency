"""Flask app for adopt app."""

import os


from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

from models import connect_db, Pet, db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_home_page():
    pets = Pet.query.all()
    return render_template("home-page.html", pets=pets)


@app.route('/add', methods=["GET","POST"])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.pet_species.data
        photo_url = form.pet_photo_url.data
        age = form.pet_age.data
        notes = form.pet_notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Sucessfully added {name}")

        return redirect("/")

    else:
        return render_template("add-pet-form.html", form = form)