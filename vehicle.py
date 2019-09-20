class Vehicle:

    def __init__(self):
        self.speed = 0.0

    def speedUp(self):
        self.speed += 10
        print(f"We are speeding up, now our speed is {self.speed}")

    def speedDown(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"We are speeding down, now our speed is {self.speed}")

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed


if __name__ == "__main__":
    vehicle = Vehicle()
    vehicle.setSpeed(60)
    print(f"Speed currently is {vehicle.getSpeed()}")
    vehicle.speedUp()
    vehicle.speedUp()
    vehicle.speedDown()
