class Dog:
    species = "Canis familiaris"

    # Constructor for the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # String representation of the Dog object
    # This is how we customise the print output for an object in its Class
    # E.g., if we do print(miles), it should return "Miles is 5 years old"
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# --------- Inheritance Examples --------- #
class GoldenRetriever(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class AmericanEskimo(Dog):
    def speak(self, sound="Arf!"):
        return super().speak(sound)

class Bulldog(Dog):
    def speak(self, sound="Woof!"):
        return super().speak(sound)
    
bob = Dog("Bob", 4)
miles = Bulldog("Miles", 5)
kenny = GoldenRetriever("Kenny", 3)

print(bob)
print(bob.speak("Woof Woof"))

print(miles)
print(miles.speak())

print(kenny)
print(kenny.speak())

print(isinstance(miles, Dog))  
