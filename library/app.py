from flask import Flask

from .database import db


app = Flask(__name__)
app.config.from_object('library.settings')

db.init_app(app)


@app.route('/hello')
def hello():
    return {'hello': 'world'}


@app.route('/books/<int:book_id>')
def get_book(book_id):
    pass


@app.route('/books')
def get_books():
    pass


@app.route('/books', methods=['POST'])
def create_book():
    pass
