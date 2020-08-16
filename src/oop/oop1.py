# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass

class FlightVehicle(Vehicle):
    #vehicle base class
    pass
class Starship(FlightVehicle):
    #FlightVehicle base class
    pass
class Airplane(FlightVehicle):
    #flightvehicle base class
    pass

class GroundVehicle(Vehicle):
    #vehicle base class
    pass
class Car(GroundVehicle):
    #GroundVehicle base class
    pass

class Motorcycle(GroundVehicle):
    #GroundVehicle base class
    pass
