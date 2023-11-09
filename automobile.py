from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

# =============================================================================
# Automobiles

AUTOMOBILES = {
    "automobile1": {"brand": "Mercedes-Benz", "model": "A Class", "body": "Hatchback", "fuel": "Petrol", "price": 31600, "seats": 5},
    "automobile2": {"brand": "Mercedes-Benz", "model": "C Class", "body": "Coupe", "fuel": "Petrol", "price": 36205, "seats": 4},
    "automobile3": {"brand": "Mercedes-Benz", "model": "G Class", "body": "SUV", "fuel": "Diesel", "price": 93965, "seats": 5},
    "automobile4": {"brand": "BMW", "model": "X3", "body": "SUV", "fuel": "Hybrid", "price": 46265, "seats": 5},
    "automobile5": {"brand": "BMW", "model": "M3", "body": "Estate", "fuel": "Petrol", "price": 84350, "seats": 5},
    "automobile6": {"brand": "BMW", "model": "i3", "body": "Hatchback", "fuel": "Electric", "price": 49995, "seats": 5},
    "automobile7": {"brand": "Toyota", "model": "Land Cruiser", "body": "SUV", "fuel": "Diesel", "price": 33480, "seats": 7},
    "automobile8": {"brand": "Toyota", "model": "Yaris", "body": "Hatchback", "fuel": "Petrol", "price": 21970, "seats": 5},
    "automobile9": {"brand": "Toyota", "model": "C-HR", "body": "SUV", "fuel": "Hybrid", "price": 26100, "seats": 5},
}

# =============================================================================

def abort_if_automobile_doesnt_exist(automobile_id):
    if automobile_id not in AUTOMOBILES:
        abort(404, message="{} doesn't exist".format(automobile_id))

parser = reqparse.RequestParser()
parser.add_argument("brand", type=str, required=True)
parser.add_argument("model", type=str, required=True)
parser.add_argument("body", type=str, required=True)
parser.add_argument("fuel", type=str, required=True)
parser.add_argument("price", type=int, required=True)
parser.add_argument("seats", type=int, required=True)

# Automobile
# shows just asked automobile item and lets us delete an automobile
class Automobile(Resource):
    def get(self, automobile_id):
        abort_if_automobile_doesnt_exist(automobile_id)
        return AUTOMOBILES[automobile_id]
    
    def delete(self, automobile_id):
        abort_if_automobile_doesnt_exist(automobile_id)
        del AUTOMOBILES[automobile_id]
        return "", 204
    
    def put(self, automobile_id):
        args = parser.parse_args()
        AUTOMOBILES = args
        return AUTOMOBILES[automobile_id], 201

# List of Automobiles
## This shows a list of all automobiles and lets us post to add new automobiles
class ListOfAutomobile(Resource):
    def get(self):
        return AUTOMOBILES

    def post(self):
        args = parser.parse_args()
        automobile_id = int(max(AUTOMOBILES.keys()).lstrip("automobile")) + 1
        automobile_id = "automobile%i" % automobile_id
        AUTOMOBILES[automobile_id] = args
        return AUTOMOBILES[automobile_id], 201

#
# Setup the API resource routing here
#
api.add_resource(ListOfAutomobile, "/automobiles")
api.add_resource(Automobile, "/automobiles/<automobile_id>")

if __name__ == "__main__":
    app.run(debug = True)
