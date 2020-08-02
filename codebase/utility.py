#utility.py

def parsedCoordinates(location):
    coOrdinates = location.split(",")
    x_cor = float(coOrdinates[0])
    y_cor = float(coOrdinates[1])
    return { "x": x_cor, "y": y_cor }

def parseCoordinates(location):
    coOrdinates = location.split(",")
    x_cor = float(coOrdinates[0])
    y_cor = float(coOrdinates[1])
    return [x_cor,y_cor]

def createUserObjectForDataBase(jsonObj):
    return {
                "firstName" : jsonObj["firstName"],
                "lastName" : jsonObj["lastName"],
                "email" : jsonObj["email"],
                "phoneNumber" : jsonObj["phoneNumber"],
                "bloodGroup" : jsonObj["bloodGroup"],
                "loc" : parsedCoordinates(jsonObj["location"]),
                "volunteerToDonate" : jsonObj["volunteerToDonate"],
                "covidStatus" : jsonObj["covidStatus"]
            }

def createChatRegistyObjectForDataBase(jsonObj):
    return {
                "id" : jsonObj["id"],
                "user1" : jsonObj["user1"],
                "user2" : jsonObj["user2"],
            }