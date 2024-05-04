"""
Filename: vehicle_app.py
Author: Lee Dillard
Created: 05/01/2024
Purpose: Create a vehicle module for import
"""

# Import vehicle module
from vehicle import Car

# TODO: Create car object
car = Car()
def set_speed(self, speed):
    self._speed = speed

# TODO: Display user name with maximum speed and number of passengers
print(f"{car.get_user_name} is driving a {car.get_car_model} that can seat {car.get_car_seating}.")
print(f"The maximum speed of the {car.get_car_model} is {car.get_max_speed} mph.")
print()

# TODO: User input with an exit statement
while True:

    choice = input(f"Start (E)ngine | (A)ccelerate | (B)rake | (S)top  | E(x)it: ")
    if choice == "e":
        print(f"The {car.get_car_model}'s engine is running.")
        print()
    elif choice == "a":
        car.accelerate()
        print(f"The {car.get_car_model} is going {car.get_speed} mph.")
        print()
    elif choice == "b":
        car.brake()
        print(f"The {car.get_car_model} is going {car.get_speed} mph.")
        print()
    elif choice == "s":
        car.stop()
        print(f"The {car.get_car_model} is going {car.get_speed} mph.")
        print()
    elif choice == "x":
        print(f"Thank you for visiting our dealership. Have a good day!")
        print()
        break

# If a standalone program, call the main function
# Else, use as a module"""
    
#if __name__ == "__main__":
    #main()