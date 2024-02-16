from flask import Blueprint, request, jsonify

user_routes = Blueprint('user_routes', __name__)

# This will store user data temporarily in memory. Replace this with a database in a real application.
#add to collection in mongo
users = []

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.json

    # Check if all required fields are present
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Check if the username is already taken
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username already exists'}), 400

    # Add the user to the list of registered users
    users.append({
        'username': username,
        'email': email,
        'password': password
    })

    return jsonify({'message': 'User registered successfully'}), 201
