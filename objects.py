
# CLASSES IN PYTHON

class Insect:
    def __init__(self):  # needs to be initialised each time we are adding attributes
        self.__compound_eyes = 2 # the __ protects the variable from being eternally changed
        self.legs = 6
        self.parts = 3
        self.wings = 2

    def eyes(self):
        pass


cockroach = Insect()  # class being inherited and also in another page using import above, then the imported file.func

print(cockroach.parts)
