from flask import Blueprint, render_template
from .controllers import login, register

user_management = Blueprint('user_management', __name__)

@user_management.route('/login', methods=['GET', 'POST'])
def login_view():
    return login()

@user_management.route('/register', methods=['GET', 'POST'])
def register_view():
    return register()
