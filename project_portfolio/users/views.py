from flask import Blueprint, render_template

user = Blueprint('users', __name__,
                 template_folder='templates',
                 static_folder='static')


@user.route('/<string:name>')
def index(name):
    return 'Hello ' + name
