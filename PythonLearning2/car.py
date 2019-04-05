class Car(): 
    def __init__(self, make, model, year): 
            """ Initialize attributes to describe a car.""" 
            self.make = make 
            self.model = model 
            self.year = year
            self.odometer_reading = 0 

    def read_odometer(self): 
        """ Print a statement showing the car's mileage.""" 
        print(" This car has " + str( self.odometer_reading) + " miles on it.")

     
    def get_descriptive_name(self): 
        """ Return a neatly formatted descriptive name.""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

class Battery(): 
    """ A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 70): 
        """ Initialize the battery's attributes.""" 
        self.battery_size = battery_size
    def describe_battery( self): 
        """ Print a statement describing the battery size.""" 
        print(" This car has a " + str( self.battery_size) + "-kWh battery.") 
        
class ElectricCar(Car):
    """ Note above ElectricCar class is child of Car class
    Represent aspects of a car, specific to electric vehicles."""
    def __init__( self, make, model, year): 
        """ Initialize attributes of the parent class. Then initialize attributes specific to an electric car. """
        super().__init__(make, model, year)
        self.battery = Battery()  # here the attribute battery is the class Battery
 
 
 



