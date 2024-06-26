"""
Filename: vehicle.py
Author: Lee Dillard
Created: 05/01/2024
Purpose: Demonstrate creating a class object with four attributes and four methods along
with user input
"""
# Import the Console module for spiffy title
from rich.console import Console

# Import the Panel module for even more spiffy title options
from rich.panel import Panel

# Initialize Console
console = Console()

# Initialize car class
class Car:
    def __init__(self, speed=55):
        self._speed = speed
        self._car_exit = exit
    # Make title for the program
    def title():
        console.print(
            Panel.fit(
            "  -->  Lucky's Car Lot  <--  ",
            style="bold red"
            )
        )

    # Get user name
    def get_user_name(self):
            self._user_name = console.input(f"[blue]Enter your name: [blue]")
            return self._user_name

    # Get car model
    def get_car_model(self):
            self._car_model = console.input(f"[blue]Enter the car you would like to drive: [blue]")
            return self._car_model

    # Get seating capacity
    def get_car_seating(self):
            self._car_seating = console.input(f"[blue]Enter how many passengers: [blue]")
            return self._car_seating

    # Get maximum speed
    def get_max_speed(self):
            self._max_speed = console.input(f"[blue]Enter the maximum speed: [blue]")
            return self._max_speed
    print()
    
    # Get speed
    def get_speed(self):
            return self._speed

    # Define the accellerate method
    def accelerate(self):
            self._speed += 5
                  
    # Define the brake method
    def brake(self):
            self._speed -= 5

    # Define the stop method
    def stop(self):
            self._speed = 0

# Initialize program

def main():
    car = Car
    Car.title()
    car.get_user_name()
    car.get_car_model()
    car.get_car_seating()
    car.get_max_speed()

