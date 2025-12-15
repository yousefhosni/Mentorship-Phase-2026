import uuid

class User:
    def __init__(self, name, user_id=None):
        self.user_id = user_id if user_id else str(uuid.uuid4())
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }
