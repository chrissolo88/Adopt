from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    specie_id = db.Column(db.Integer,  db.ForeignKey('species.id'), nullable=False)
    photo_url = db.Column(db.Text,nullable=False, default="https://thumbs.dreamstime.com/b/empty-dog-bowl-outline-icon-empty-dog-bowl-outline-icon-clipart-image-isolated-white-background-139839179.jpg")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    specie = db.relationship("Specie", backref="pets")
    
    def __repr__(self):
        return f"<Pet {self.name} {self.specie.specie} {self.age} >"
    
class Specie(db.Model):
    
    __tablename__ = "species"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    specie = db.Column(db.Text, nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Specie {self.specie}>"
    
    
    
