import pymongo

class users_db:
    def __init__(self):
        self.db = db_control()
        self.client = self.db.get_client()
        self.db_users = self.client["users_db"]
        self.users = self.db_users["users"]

    def push_form(self, id, query):
        try:
            x = self.users.update_one({"id" : id}, query)
        except pymongo.errors.PyMongoError:
            return False
        return True
