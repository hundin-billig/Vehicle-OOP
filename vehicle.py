"""
Filename: vehicle.py
Author: Lee Dillard
Created: 04/22/2024
Purpose: Create a vehicle module for import
"""

# Initialize the Vehicle object with 4 parameters
class Vehicle:
    def __init__(self, _name, _vehicle, _passenger, _speed):
    self._name = _name
    self._vehicle = _vehicle
    self._passenger = _passenger
    self._speed = _speed

    # Define get_name
    def get_name(self):
        return self._name

    # Define get_vehicle
    def get_vehicle(self):
        return self._vehicle

    # Define get_passenger
    def get_passenger(self):
        return self._passenger

    # Define get_speed
    def get_speed(self):
        return self._speed
    
    # Define the accellerate method
    def accelerate(self):
            self._speed += 5

    # Define the brake method
    def brake(self):
            self._speed -= 5
