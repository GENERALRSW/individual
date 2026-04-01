from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    no_of_rooms = IntegerField('No. of Rooms', validators=[DataRequired(), NumberRange(min=1)])
    no_of_bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
    ])
