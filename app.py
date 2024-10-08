from flask import Flask
from flask_migrate import Migrate
import os
from models import db  # Import the shared db instance
from user_management.views import user_management
from sensor_data.views import sensor_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize the shared database instance
db.init_app(app)
migrate = Migrate(app, db)
# Register Blueprints
app.register_blueprint(user_management)
app.register_blueprint(sensor_data)

with app.app_context():
    db.create_all()  # Create all tables for both user management and sensor data

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
