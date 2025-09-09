"""
Task 2: Create a class named Car with attributes like make, model, year, colour, and kilometerage.
Include methods such as speed(), accelerate(), brake(), repaint(), and service().
Then, create two child classes named Haval and Toyota that inherit from the Car class.
Override at least one method in each child class to demonstrate polymorphism."""

class Car:
    def __init__(self, make, model, year, colour, kilometerage):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.kilometerage = kilometerage
        self.speed = 0  

    def __str__(self):
        return f"This {self.colour} {self.make} car has {self.kilometerage} kilometers."
    
    def motorType(self, motor_type):
        return f"This car has a {motor_type} motor."

    def speed(self, units):
        return f"Current speed: {self.speed} {units}."
    
    def accelerate(self, increase):
        self.speed += increase
        return f"Accelerated to {self.speed} km/h."
    
    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        return f"Slowed down to {self.speed} km/h."
    
    def repaint(self, new_colour):
        self.colour = new_colour
        return f"The car has been repainted to {self.colour}."

    def service(self, is_serviced):
        if is_serviced:
            return "The car is being serviced."
        else:
            return "The car does not need servicing."
    
class Haval(Car):
    """
    A child class representing a Haval car.
    Inherits from Car and overrides the speed() method.
    """
    def __init__(self, model, year, colour, kilometerage):
        # We call the parent's __init__ method, hardcoding 'Haval' for the make.
        super().__init__('Haval', model, year, colour, kilometerage)

    def speed(self, description='fast'):
        """
        Overrides the parent's speed method with a default value for the argument
        """
        if description == 'fast':
            return f"This {self.make} {self.model} is going really fast!"
        else:
            # If a different description is provided, we can call the parent method
            # to get a standard speed reading.ß 
            return super().speed(description)
        
    def offroad(self, terrain_type):
        return f"The {self.make} {self.model} is driving offroad on {terrain_type} terrain."

class Toyota(Car):
    """
    A child class representing a Toyota car.
    Inherits from Car and overrides the speed() method.
    """
    def __init__(self, model, year, colour, kilometerage):
        # We call the parent's __init__ method, hardcoding 'Toyota' for the make.
        super().__init__('Toyota', model, year, colour, kilometerage)

    def speed(self, description='steady'):
        """
        Overrides the parent's speed method with a default value for the argument
        """
        if description == 'steady':
            return f"This {self.make} {self.model} is cruising at a steady pace."
        else:
            # If a different description is provided, we can call the parent method
            # to get a standard speed reading.ß 
            return super().speed(description)
        
    def motorType(self, motor_type):
        return super().motorType(motor_type) + " It is known for its reliability."


''' *--------- An Example of Transitive Inheritance --------- # '''
class Corolla(Toyota):
    def __init__(self, year, colour, kilometerage):
        super().__init__('Corolla', year, colour, kilometerage)