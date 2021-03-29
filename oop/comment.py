# A class with instance variables
class Comment:
    """
    This class is a social media application comment class. It has the following attributes:
    1. Username - The commenter's username.
    2. text - the comment text.
    3. likes - the number of likes the comment received.
    """
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes