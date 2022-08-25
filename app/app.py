from flask import Flask, render_template
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

# Выполнить в консоли
# python -m flask db init
# python -m flask db migrate -m "Initial migration."
# python -m flask db upgrade




