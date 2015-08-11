import os

from flask import Flask

import server_settings as config
from project.views import project
from users.views import user

app = Flask(__name__)

# Blueprints
app.register_blueprint(project, url_prefix='/project')
app.register_blueprint(user, url_prefix='/user')

# Server start
port = config.PORT if config.DEBUG else int(os.environ.get('PORT', 5000))
app.run(host=config.HOST, port=port, debug=config.DEBUG)
