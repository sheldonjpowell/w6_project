from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dont guess'

from app import routes