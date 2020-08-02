from flask import Blueprint
from flask import Flask
from .extensions import mongo
from flask import json
from flask import request
import json
from .utility import parsedCoordinates, parseCoordinates, createUserObjectForDataBase, createChatRegistyObjectForDataBase
from bson.json_util import dumps
from flask_cors import CORS,cross_origin


main = Blueprint('main', __name__)
CORS(main)

#TestConnectivity
@main.route('/')
def hello():
    return "Test Connectivity Successful"

#Returning Random User
@main.route('/users')
def getAll():
    user_collection = mongo.db.hackcollection
    return dumps(user_collection.find_one())

#Register New User
@main.route('/register', methods=['POST','PUT'])
def register():
    user_collection = mongo.db.hackcollection
    #need to improve validation here
    if user_collection.find({"email": request.json["email"]}).count() is 0:
        user_collection.insert(createUserObjectForDataBase(request.json))
        return json.dumps(request.json)
    else:
        return "Email already registered"
        raise Exception("Email registered")

#Get Location Based Users
@main.route('/<location>/<int:radius>/', methods=['GET'])
def getLocBasedUsers(location,radius):
    user_collection = mongo.db.hackcollection
    cor = parseCoordinates(location)

    #radius needs to be passed in kilometres
    myquery = { "loc": { "$geoWithin": { "$center": [ [cor[0], cor[1]], radius/111.3 ] } } , "volunteerToDonate" : "True"}
    return (dumps(user_collection.find(myquery)))

#Get Blood Group, Location Bases Users
@main.route('/<bloodGroup>/<location>/<int:radius>/', methods=['GET'])
def getValidUsers(bloodGroup,location,radius):
    user_collection = mongo.db.hackcollection
    cor = parseCoordinates(location)

    #radius needs to be passed in kilometres
    myquery = { "loc": { "$geoWithin": { "$center": [ [cor[0], cor[1]], radius/111.3 ] } } , "bloodGroup" : bloodGroup, "volunteerToDonate" : "True"}
    return (dumps(user_collection.find(myquery)))

@main.route('/user/<email>')
def profile(email):
    user_collection = mongo.db.hackcollection
    myquery = { "email": email}
    return dumps(user_collection.find(myquery))

@main.route('/chat/register', methods=['POST','PUT'])
def registerForChatDb():
    chatRegistry = mongo.db.chatRegistry
    if chatRegistry.find({"user1" : request.json["user1"], "user2" : request.json["user2"]}).count() is 0:
        chatRegistry.insert(createChatRegistyObjectForDataBase(request.json))
        return json.dumps(request.json)
    else:
        return "user pair is already in registry"

@main.route('/chat/get/', methods=['GET'])
def getAllChat():
    chatRegistry = mongo.db.chatRegistry
    return dumps(chatRegistry.find())
