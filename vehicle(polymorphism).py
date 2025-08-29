# Activity 2: POLYMORPHISM CHALLENGE

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(vehicle):
    def move(self):
        print("this car is moving on land")

class Plane(vehicle):
    def move(self):
        print("this plane is flying in the air")

class Boat(vehicle):
    def move(self):
        print("this boat is sailing in the ocean")


car=Car()
plane=Plane()
boat=Boat()

vehicles=[Car(),Plane(),Boat()]
for vehicle in vehicles:
    vehicle.move()
