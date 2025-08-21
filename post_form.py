from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
