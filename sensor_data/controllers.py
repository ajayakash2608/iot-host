from flask import request, jsonify
from .models import SensorData, db
from datetime import datetime, timedelta, timezone
import pytz
def receive_data():
    if request.is_json:  # Check if the request is JSON
        data = request.get_json()  # Use get_json() for better error handling
        
        # Create new SensorData instance with current timestamp
        new_data = SensorData(
            temperature=data['temperature'], 
            humidity=data['humidity'],
            hb=data['hb'],
            timestamp=datetime.now(timezone.utc)  # Set current UTC time
        )
        
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"status": "success"}), 201
    
    return jsonify({"error": "Request must be JSON"}), 400

def get_sensor_data():
    all_data = SensorData.query.all()
    # Convert timestamp to formatted string in the dictionary
    return [
        {
            **data.to_dict(),
            "timestamp": data.timestamp.strftime('%d-%b-%Y %I:%M %p')  # Format timestamp
        } for data in all_data
    ]



def update_sensor_data(data_id, data):
    sensor_data = SensorData.query.get(data_id)
    if sensor_data:
        sensor_data.temperature = data.get('temperature', sensor_data.temperature)
        sensor_data.humidity = data.get('humidity', sensor_data.humidity)
        sensor_data.hb = data.get('hb', sensor_data.hb)  # Update hb if provided
        
        # Update the timestamp to the current time in UTC
        sensor_data.timestamp = datetime.now(timezone.utc)  # Get current time in UTC
        
       
        
        db.session.commit()
        return {
            **sensor_data.to_dict(),
            "timestamp": sensor_data.timestamp.strftime('%d-%b-%Y %I:%M %p')  # Format timestamp in IST
        }


def delete_sensor_data(data_id):
    sensor_data = SensorData.query.get(data_id)
    if sensor_data:
        db.session.delete(sensor_data)
        db.session.commit()
        return True
    return False
