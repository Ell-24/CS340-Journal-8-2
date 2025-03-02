from pymongo import MongoClient
from bson.objectid import ObjectId

#Must be utilized after importing the database and setting up authentication account
#please ensure port and Database have the correct names
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        #Initialize connection
        #Connect Variables
        #This is utilized for verification and Server and database connection/identification
        USER = "aacuser2"
        PASS = "SNHU1234"
        HOST = "nv-desktop-services.apporto.com"
        PORT = 32392
        DB = "AAC"
        COL = "animals"

        #Connect to server
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data) #data should be dictionary 
            if result.inserted_id:  # return true if function was successfully executed
                return True
            else:
                return False
        else:   #if the parameters is empty throw an error
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is None: #if data isnt found
            return list(self.collection.find())
        else: #if data is found read out the identified data
            return list(self.collection.find(data))

        
    #Create method to implement the U in CRUD
    def update(self, data, new_data):
        if data is None:  #throw error if it cant be found
            raise Exception("Query cannot be found")
        result = self.collection.update_many(data, {"$set": new_data}) #Update function
        if result.modified_count > 0: #return true if function was successfully executed
            return True
        else:
            return False
        
            
    #Create method to implement the D in CRUD
    def delete(self, data):
        if data is None:  #throw error if it cant be found
            raise Exception("Query cannot be found")
        result = self.collection.delete_one(data) #Delete function
        if result.deleted_count > 0:  #return true if function was successfully executed
            return True
        else:
            return False