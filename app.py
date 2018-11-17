from flask import Flask
from keystonemiddleware import auth_token

app = Flask(__name__)

KEYSTONE_AUTHTOKEN = {
    'auth_url': 'http://10.5.9.58:5000/v3',
    'auth_plugin': 'password',
    'username': 'admin',
    'password': 'vccloud',
    'project_name': 'admin',
    'user_domain_name': 'default',
    'project_domain_name': 'default'
}

app.wsgi_app = auth_token.AuthProtocol(app.wsgi_app, KEYSTONE_AUTHTOKEN)


@app.route("/")
def index():
    """
    Test authen
    """
    return "Authenticated"  


if __name__ == '__main__':
    app.run(debug=True)
