from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, Specie
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abc123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['WTF_CSRF_ENABLED'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    pets_available = Pet.query.filter_by(available=True).all()
    pets_adopted = Pet.query.filter_by(available=False).all()
    return render_template('home.html', pets_available=pets_available, pets_adopted=pets_adopted)

@app.route('/pets/add', methods=['POST', 'GET'])
def add_pet():
    form = AddPetForm()
    species = [(s.specie,s.specie) for s in Specie.query.all()]
    form.specie.choices = species
    if form.validate_on_submit():
        name = form.name.data
        specie = Specie.query.filter_by(specie=form.specie.data).one()
        age = int(form.age.data)
        notes = form.notes.data
        photo_url = form.photo_url.data
        photo_url = photo_url if photo_url else None
        pet = Pet(name=name, specie_id=specie.id, age=age,notes=notes,photo_url=photo_url)
        
        db.session.add(pet)
        db.session.commit()
        flash(f'Added New Pet Name:{name} Species:{form.specie.data}', 'success')
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/pets/<int:pet_id>')
def view_pet(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('view_pet.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    form = AddPetForm()
    pet = Pet.query.get(pet_id)
    species = [(s.specie,s.specie) for s in Specie.query.all()]
    form.specie.choices = species
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.specie = Specie.query.filter_by(specie=form.specie.data).one()
        pet.age = int(form.age.data)
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f'Editied Pet Name:{pet.name} Species:{form.specie.data}', 'success')
        return redirect(f'/pets/{pet_id}')
    else:
        form.name.data = pet.name
        form.specie.data = pet.specie.specie
        form.age.data = pet.age
        form.notes.data = pet.notes
        form.photo_url.data = pet.photo_url
        return render_template('edit_pet_form.html', form=form, pet=pet)
    
@app.route('/pets/<int:pet_id>/adopt', methods=['GET', 'POST'])
def adopt_pet(pet_id):
    pet = Pet.query.get(pet_id)
    pet.available = False
    db.session.commit()
    flash(f'Amazing! {pet.name} Was Adopted!', 'success')
    return redirect(f'/')