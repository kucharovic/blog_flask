from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

from app.blog.controllers import blog as blog_module

app.register_blueprint(blog_module)

db.create_all()