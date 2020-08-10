import pymongo
from src import db_control


class users_db:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db_users = self.client["users_db"]
        self.users = self.db_users["users"]

    def push_form(self, id, query):
        try:
            x = self.users.update_one({"id" : id}, query)
        except pymongo.errors.PyMongoError:
            return False
        return True
