from flask import Blueprint, render_template, jsonify, request
from .controllers import receive_data, get_sensor_data,update_sensor_data,delete_sensor_data

sensor_data = Blueprint('sensor_data', __name__, template_folder='templates')  # Specify the template folder

@sensor_data.route('/data', methods=['POST'])
def post_data():
    return receive_data()

@sensor_data.route('/data', methods=['GET'])
@sensor_data.route('/data', methods=['GET'])
def list_sensor_data_view():
    all_data = get_sensor_data()

    # Replace None values with 0 for all fields
    for data in all_data:
        for key in data:
            if data[key] is None:
                data[key] = 0

    return render_template('sensor_data.html', sensor_data=all_data)



@sensor_data.route('/data/json', methods=['GET'])
def sensor_data_json():
    all_data = get_sensor_data()
    return jsonify(all_data)

@sensor_data.route('/post', methods=['GET'])
def post_sensor_data_view():
    return render_template('post_data.html')
# Route to update existing sensor data
@sensor_data.route('/data/<int:data_id>', methods=['PUT'])
def update_sensor_data_view(data_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    updated_data = update_sensor_data(data_id, data)  # Call the controller function to update
    if updated_data:
        return jsonify(updated_data), 200
    return jsonify({"error": "Data not found"}), 404

# Route to delete sensor data
@sensor_data.route('/data/<int:data_id>', methods=['DELETE'])
def delete_sensor_data_view(data_id):
    result = delete_sensor_data(data_id)  # Call the controller function to delete
    if result:
        return jsonify({"message": "Data deleted successfully"}), 200
    return jsonify({"error": "Data not found"}), 404
