class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def describe(self):
        return f"The {self.name} moves at a speed of {self.speed} km/h."


class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def describe(self):
        return f"The car {self.name} runs on {self.fuel_type} and moves at {self.speed} km/h."


class Bike(Vehicle):
    def __init__(self, name, speed, type_of_bike):
        super().__init__(name, speed)
        self.type_of_bike = type_of_bike

    def describe(self):
        return f"The bike {self.name} is a {self.type_of_bike} bike and moves at {self.speed} km/h."


# Example usage
car = Car("Toyota", 120, "Petrol")
bike = Bike("Yamaha", 80, "Sports")

print(car.describe())
print(bike.describe())
