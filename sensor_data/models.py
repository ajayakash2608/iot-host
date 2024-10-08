from models import db  # Import the shared db instance
from datetime import datetime

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=True,default='0')
    humidity    = db.Column(db.Float, nullable=True,default='0')
    hb          = db.Column(db.Float, nullable=True,default='0')
    timestamp = db.Column(db.DateTime,nullable=True, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'hb'       :self.hb,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,  # Guard against None
        }
