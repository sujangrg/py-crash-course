class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You cannot enter negative number:")
        else:
            self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
#print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# my_used_car = Car('subaru', 'outback', 2019)
# #print(my_new_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()




