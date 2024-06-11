

class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors=None):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

bilding = House(0)
print(bilding.numberOfFloors)
bilding.setNewNumberOfFloors(5)


