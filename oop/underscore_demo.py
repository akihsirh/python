class UnderscoreDemo:
    """
    This class demonstrates use of underscores in variables and method names
    """

    def __init__(self):
        self.public_var = "Public"
        self._weak_private_var = "Weak Private"
        self.__mangled_var = "Mangled"
        self.try_ = "Reserved confusion avoidance"


# Print class variables
demo = UnderscoreDemo()
print(demo.public_var)
print(demo._weak_private_var)
print(demo.try_)
print("You will observe an error in the following statement because of an attempt to print a mangled variable.")
print(demo.__mangled_var)
