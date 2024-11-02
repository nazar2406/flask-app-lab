from flask import Flask
app = Flask(__name__, template_folder='templates')
app.config.from_pyfile("../config.py")

from . import view

# from app.post import post_bp
# app.register_blueprint(post_bp)

from app.users import users_bp
app.register_blueprint(users_bp)