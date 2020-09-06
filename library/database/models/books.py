from .. import db
from ..relations import book_author
from .mixins import TimestampMixin


class Book(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    isbn = db.Column(db.Integer)
    authors = db.relationship('Author', secondary=book_author,
                              lazy='subquery', backref=db.backref(
                                  'books', lazy=True))
