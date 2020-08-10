import pymongo

class db_control:
    def __init__(self):
        self.client = pymongo.MongoClient("MONGODB_IP_PORT")


    #####   CONNECTIONS #####

    def get_client(self):
        return self.db_data
