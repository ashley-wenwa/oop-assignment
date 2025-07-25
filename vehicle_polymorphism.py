# Activity 2: Polymorphism with Vehicles

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water. 🚢")

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()
