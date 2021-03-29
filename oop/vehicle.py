# A class with __repr__ method example
class Vehicle:
    """
        The vehicle class has the following attributes:
        1. make - The brand of the vehicle.
        2. model - the product name.
        3. year - the year the vehicle was made.
        """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        """
        This function prints vehicle information.
        Returns: The make, model and year of the vehicle.

        """
        return f"This vehicle is a {self.make} {self.model}. It was made in {self.year}."

# instantiate a new Vehicle and save it to a variable called car:
car = Vehicle("Toyota", "Camry", "1982")

# instantiate a new Vehicle and save it to a variable called boat:
boat = Vehicle("Sabre", "48 Salon Express", "2011")

#print vehicles
print(boat)
print(car)
