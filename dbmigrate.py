from flask_migrate import Migrate
from app import app, db  # Adjust the import to your structure

migrate = Migrate(app, db)
