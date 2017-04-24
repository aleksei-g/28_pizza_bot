from flask import Flask, request, Response
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Pizza, PizzaChoices
from database import db_session
from os import getenv
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class PizzaModelView(ModelView):
    def check_auth(self, username, password):
        return username == USER_NAME and password == PASSWORD

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


SECRET_KEY = getenv('SECRET_KEY')
USER_NAME = getenv('USER_NAME')
PASSWORD = getenv('PASSWORD')
if not SECRET_KEY or not USER_NAME or not PASSWORD:
    raise Exception('SECRET_KEY, USER_NAME and PASSWORD should be specified')
app = Flask(__name__)
app.secret_key = SECRET_KEY
admin = Admin(app, name='Pizza', template_mode='bootstrap3')
admin.add_view(PizzaModelView(Pizza, db_session))
admin.add_view(PizzaModelView(PizzaChoices, db_session))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
