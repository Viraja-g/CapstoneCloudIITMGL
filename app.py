from flask import Flask

from Routes.User_routes import user_routes
from Routes.Driver_routes import driver_routes

from Routes.Ride_routes import ride_routes

app = Flask(__name__)

app.register_blueprint(user_routes)
app.register_blueprint(driver_routes)
app.register_blueprint(ride_routes)

@app.route('/')
def index():
    return 'Welcome to the Ride-Sharing Application!!'

if __name__ == '__main__':
    app.run(debug=True)
