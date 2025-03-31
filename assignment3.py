class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass  # Placeholder method


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # Call the base class constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()  # Call the base class method (even if it does nothing)
        return self.width * self.height


# Example usage
rect = Rectangle("MyRectangle", 5, 10)
print(f"The area of {rect.name} is {rect.calculate_area()}.")
