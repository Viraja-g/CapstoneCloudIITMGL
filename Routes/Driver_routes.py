from flask import Blueprint, request, jsonify

driver_routes = Blueprint('driver_routes', __name__)

# This will store driver data temporarily in memory. Replace this with a database in a real application.
drivers = []

@driver_routes.route('/register_driver', methods=['POST'])
def register_driver():
    data = request.json

    # Check if all required fields are present
    if 'username' not in data or 'email' not in data or 'password' not in data or 'car_type' not in data or 'car_details' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    username = data['username']
    email = data['email']
    password = data['password']
    car_type = data['car_type']
    car_details = data['car_details']

    # Check if the username is already taken
    if any(driver['username'] == username for driver in drivers):
        return jsonify({'error': 'Username already exists'}), 400

    # Add the driver to the list of registered drivers
    drivers.append({
        'username': username,
        'email': email,
        'password': password,
        'car_type': car_type,
        'car_details': car_details
    })

    return jsonify({'message': 'Driver registered successfully'}), 201

