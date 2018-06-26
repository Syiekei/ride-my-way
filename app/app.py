from flask import flask, jsonify, request

app = Flask(_name_)
rides = [
    {
        'car': 'Ride-with-me App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers',
        'rides' : [
            {
                'car':'My Rides'
                'fare':20.0
            }
        ]
    
    }
    }
]
# POST - used to receive data
# GET - used to send data back only

# POST /api/v1: {car:}
@app.route('/api/v1/rides', meethods=['POST'])
def create_api():
    request_rides = request.get_json()
    new_rides = {
        'car': request_rides['name'],
        'rides':[]
    }
    rides.append(new_rides)
    return jsonify(new_rides)

# GET /api/v1/rides:car>
@app.route('/api/v1/<rides:car>', methods=['GET'])
def get_api(car):
    for api in api:
        if api['car'] == car:
            return jsonify(api)
    return jsonify({'message': 'api not found'})

# GET /api
@app.route('/api')
def get_api():
    return jsonify({'api': api})    
    
# POST /api/v1/<rides:car>/rides {car:, fare:}
@app.route('/api/v1/<rides:car>/rides', methods=['POST'])
def create_rides_in_api(car):
    pass

# GET /api/<v1:car>/rides
@app.route('/api/<v1:car>/rides')
def get_rides_in_api(car):
    for api in api:
        if api['car'] == car:
            return jsonify({'rides': api['rides']})
    return jsonify({'message': 'api not found'})

    
    new_rides = {
        
    }
    return "Get, rides!"
    """
GET /all/rides

@app.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_single_ride(ride_id):

GET /single/ride

ride = [ride for ride in RIDES if ride['id'] == ride_id]
if ride == [ ]:
    abort(404)
return jsonify({'ride': ride[0]})

@app.route('/api/v1/rides', methods=['POST'])
def create_ride():      
    pass