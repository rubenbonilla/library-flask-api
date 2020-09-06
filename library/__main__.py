from .app import app, db
from .database.models import *  # noqa: 501
from .database.relations import *  # noqa: 501


db.create_all(app=app)
app.run(host='0.0.0.0')
