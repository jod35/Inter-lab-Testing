from lab import db
from lab.models import User,Sample
db.drop_all()
db.create_all()
