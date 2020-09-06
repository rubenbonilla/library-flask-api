from .. import db
from .mixins import TimestampMixin


class Author(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
