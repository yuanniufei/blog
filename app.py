from flask import Flask, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'hello world: {user_agent}'.format(user_agent=user_agent)


if __name__ == '__main__':
    manager.run()
