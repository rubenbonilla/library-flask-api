import os


SQLALCHEMY_DATABASE_URI = os.getenv(
    'SQLALCHEMY_DATABASE_URI', 'mysql://root:password@127.0.0.1/library')

SQLALCHEMY_TRACK_MODIFICATIONS = bool(
    int(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', '0')))

FLASK_ENV = os.getenv('FLASK_ENV', 'development')
