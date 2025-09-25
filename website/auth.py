from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<h1>login page</h1>"

@auth.route('/logout')
def logout():
    return "<h1>logout page</h1>"

@auth.route('/signUp')
def signUp():
    print("Displaying login page")
    return "<h1>signUp page</h1>"