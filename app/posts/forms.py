from wtforms import Form, StringField, TextAreaField
from wtforms.validators import InputRequired, Email

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

# Я сделал проверку на условие title = ""
# можно сделать так было, воспользоваться стандартным валидатором wtforms
    # title = StringField('Title',[validators.Length(min=5, max=40)])
    # body = TextAreaField('Body',[validators.Length(min=5, max=10000)])


# class BaseUserForm(Form):
#     name = StringField('Name')
#     email = TextAreaField('Email')