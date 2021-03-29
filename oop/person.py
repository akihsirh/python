# A class with instance variables and methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_intro(self):
        """
        This function prints the name and age of the person via an intro.
        """
        print(f"Hi, {self.first_name} {self.last_name} here. I'm {self.age} years old.")


# set persons
person1 = Person("Joe", "Tribbiani", 39)
person2 = Person("Rachel", "Green", 39)

# print persons
person1.print_intro()
person2.print_intro()
