class User:
    """A class for the user his name and age"""
    def __init__(self, userName, age):
        self.username = userName
        self.age = age
    def GetStatus(self):
        ''' A function that checks which state a user is in'''
        if self.age < 13:
            print(f"{self.username}, you are considered a child!")  # Press Ctrl+F8 to toggle the breakpoint.
        elif self.age > 18:
            print(f"{self.username}, you are considered an adult!")  # Press Ctrl+F8 to toggle the breakpoint.
        else:
            print(f"{self.username}, you are considered a teenager!")  # Press Ctrl+F8 to toggle the breakpoint.
