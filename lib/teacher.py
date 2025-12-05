from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Predefined knowledge list
        self.knowledge = [
            "Math", "Science", "History", "Art", "Physical Education"
        ]

    def teach(self):
        # Returns a random piece of knowledge
        return random.choice(self.knowledge)