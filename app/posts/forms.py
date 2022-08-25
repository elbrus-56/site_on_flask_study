from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

# Я сделал проверку на условие title = ""
# можно сделать так было, воспользоваться стандартным валидатором wtforms
    # title = StringField('Title',[validators.Length(min=5, max=40)])
    # body = TextAreaField('Body',[validators.Length(min=5, max=10000)])