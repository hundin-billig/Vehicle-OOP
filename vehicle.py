"""
Filename: vehicle.py
Author: Lee Dillard
Created: 05/01/2024
Purpose: Demonstrate creating a class object with four attributes and four methods along
with user input
"""
# Import the Console module for spiffy title
from rich.console import Console
# Import the Panel module for more spiffy title options
from rich.panel import Panel
# Initialize Console
console = Console()

# TODO: Initialize car class
class Car:
    def __init__(self, speed=55):
        self._speed = speed

       
    # TODO: Make title for the program
    def title():
        console.print(
            Panel.fit(
            "  -->  Lucky's Car Lot  <--  ",
            style="bold red"
            )
        )

    # TODO: Get user name
    def get_user_name(self):
            self._user_name = input("Enter your name: ")
            return self._user_name

    # TODO: Get car model
    def get_car_model(self):
            self._car_model = input(f"Enter the car you would like to drive: ")
            return self._car_model

    # TODO: Get seating capacity
    def get_car_seating(self):
            self._car_seating = input(f"Enter how many passengers: ")
            return self._car_seating

    # TODO: Get maximum speed
    def get_max_speed(self):
            self._max_speed = input(f"Enter the maximum speed: ")
            return self._max_speed
    
    # TODO: Get speed
    def get_speed(self):
            return self._speed

    #TODO: # Define the accellerate method
    def accelerate(self):
            self._speed += 5
                  
    #TODO: Define the brake method
    def brake(self):
            self._speed -= 5

    #TODO: Define the stop method
    def stop(self):
            self._speed = 0



# TODO: Initialize program

def main():
    car = Car
    Car.title()
    car.get_user_name()
    car.get_car_model()
    car.get_car_seating()
    car.get_max_speed()

