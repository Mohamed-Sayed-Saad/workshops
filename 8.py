import json

#Defining Class Router
class Router():

    #define initial parameters (hostname,  ip address, device model, oprating system version)
    def __init__(self, hostname, ipAddress, devModel, iosVersion):
        self.ipAddress = ipAddress
        self.devModel = devModel
        self.iosVersion = iosVersion
        self.hostname = hostname

    #defining get decription function which returns router's data
    def getdesc(self):
        desc = """
        hostname: {}
        Model: {}
        version: {}
        ip address: {}
        """.format(self.hostname, self.devModel, self.iosVersion, self.ipAddress)
        return desc


#Defining Class Switch which inherit from class router
class Switch(Router):

    #defining get decription function which returns switch's data
    def getdesc(self):
        desc = """
        hostname: {}
        Model: {}
        version: {}
        ip address: {}
        """.format(self.hostname, self.devModel, self.iosVersion, self.ipAddress)
        return desc


#opening external json file and decoding data into dictionary 
with open("routers.json") as data:
    jsonData = data.read()
    jsonDict = json.loads(jsonData)

#defining empty list for storing router objects
routers = []

#iterating on routers in json imported dictionary
for i in  jsonDict["routers"]:

    for item in jsonDict["routers"][i]:

        #storing values into variables
        if item == "ip address":
            ipAddr =  jsonDict["routers"][i][item]
        elif item == "version":
            version =  jsonDict["routers"][i][item]
        elif item == "model":
            model =  jsonDict["routers"][i][item]
        elif item == "hostname":
            hostname =  jsonDict["routers"][i][item]

    #intiating router object with pulled values
    routers.append(Router(hostname, ipAddr, model, version))

