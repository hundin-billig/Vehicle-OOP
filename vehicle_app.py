"""
Filename: vehicle_app.py
Author: Lee Dillard
Created: 05/01/2024
Purpose: Create a vehicle module for import
"""

# Import the Console module for spiffy title
from rich.console import Console
# Import the Panel module for more spiffy title options
from rich.panel import Panel
# Initialize Console
console = Console()
# Import vehicle module
from vehicle import Car

# Create car object
car = Car()

# Call the title of the program
Car.title()

# Call methods
user_name = car.get_user_name()
car_model = car.get_car_model()
car_seating = car.get_car_seating()
max_speed = car.get_max_speed()

# Display user name with maximum speed and number of passengers
console.print(f"[yellow]{user_name} is driving a {car_model} that can seat {car_seating}.[yellow]")
console.print(f"[yellow]The maximum speed of the {car_model} is {max_speed} mph.[yellow]")
print()

# TODO: User input with an exit statement
while True:

    choice = console.input(f"[bold white]Start (E)ngine | (A)ccelerate | (B)rake | (S)top  | E(x)it: [bold white]").lower()
    if choice == "e":
        console.print(f"[bold green]The {car_model}'s engine is running.[bold green]")
        print()
    elif choice == "a":
        car.accelerate()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()
    elif choice == "b":
        car.brake()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()
    elif choice == "s":
        car.stop()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()
    elif choice == "x":
        console.print(f"[bold green]Thank you for visiting our dealership. Have a good day![bold green]")
        print()
        break



# If a standalone program, call the main function
# Else, use as a module"""
    
#if __name__ == "__main__":
    #main()