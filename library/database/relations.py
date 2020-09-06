from . import db


book_author = db.Table('book_author',
                       db.Column('book_id', db.Integer, db.ForeignKey(
                           'book.id'), primary_key=True),
                       db.Column('author_id', db.Integer, db.ForeignKey(
                           'author.id'), primary_key=True)
                       )
