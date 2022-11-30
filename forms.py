from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    specie = SelectField("Species", validators=[InputRequired()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0,max=30)])
    photo_url = StringField("Photo URL", validators=[Optional(),URL(require_tld=True,message=None)] )
    notes = StringField("Notes", validators=[Optional()])
    
    
