class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

def process_sound(sound_object):
    print(sound_object.make_sound())

# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # Outputs: Woof!
process_sound(cat)  # Outputs: Meow!
