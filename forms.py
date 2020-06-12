from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    publishment_date = StringField('publishment_date', validators=[DataRequired()])
    description = TextAreaField('description')
    image = FileField("image")


class UploadForm(FlaskForm):
    image = FileField("image")
    description_img = TextAreaField("description_img")

