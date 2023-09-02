"""Flask app for adopt app."""

import os


from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm

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
    """homepage loads current pets"""
    pets = Pet.query.all()
    return render_template("home-page.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """renders form to add a pet"""
    form = PetForm()

    if form.validate_on_submit():
        # form.data.items return dictionary
        # if key != csrf_token

        name = form.name.data
        species = form.species.data

        # pet = Pet(**values) where dictionary has key-value pairs that are the same,

        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        # print("type of species is", type(species))
        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Sucessfully added {name}")

        return redirect("/")

    else:
        return render_template("add-pet-form.html", form=form)


@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """renders from to edit pet"""
    edit_pet = Pet.query.get(id)

    form = PetForm(obj=edit_pet)

    if form.validate_on_submit():
        edit_pet.name = form.name.data
        edit_pet.species = form.species.data.upper()
        edit_pet.photo_url = form.photo_url.data
        edit_pet.age = form.age.data
        edit_pet.notes = form.notes.data

        db.session.commit()

        flash(f"Successfully edited {edit_pet.name}")

        return redirect("/")

    else:
        return render_template("edit-pet-form.html", form=form)
