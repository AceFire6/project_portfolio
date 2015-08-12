#!venv/bin/python

from project_portfolio import app

app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)
