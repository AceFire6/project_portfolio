from flask import Blueprint, render_template

project = Blueprint('project', __name__,
                    template_folder='templates',
                    static_folder='static')


@project.route('/<int:project_id>')
def index(project_id):
    return 'Viewing ' + project_id
