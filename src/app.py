from flask import Flask
from routes.systemLogin import systemlogin
from routes.systemControl import systemcontrol
from routes.systemLibros import systemlibros

app = Flask(__name__)


app.register_blueprint(systemlogin)
app.register_blueprint(systemcontrol)
app.register_blueprint(systemlibros)

app.secret_key= 'password123'

if __name__ == '__main__':
    app.run(debug=True)