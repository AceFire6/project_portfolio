from flask import Flask

from project.views import project
from users.views import user

app = Flask(__name__)

app.config.from_pyfile('server_settings.py')

# Blueprints
app.register_blueprint(project, url_prefix='/project')
app.register_blueprint(user, url_prefix='/user')

from project_portfolio import views
