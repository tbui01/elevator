class Elevator:
    def __init__(self, currentfloor, minfloor, maxfloor):
        self.currentfloor = currentfloor
        self.floors = range(minfloor, maxfloor + 1)
        self.departs = []
        self.destinations = []

    def goUp(self):
        self.currentfloor += 1
        print("Elevator go up to floor {}".format(self.currentfloor))

    def goDown(self):
        self.currentfloor -= 1
        print("Elevator go down to floor {}".format(self.currentfloor))
