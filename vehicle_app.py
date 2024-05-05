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
# Install pygame
# pip install pygame
# Import pygame for audio control
import pygame
# Import vehicle module
from vehicle import Car

# Create car object
car = Car()

# Call the title of the program
Car.title()

# Initialize mixer for audio control
pygame.mixer.pre_init(
    44100,    # frequency
    16,       # bit
    2,        # stereo
    4096      # buffer size
    )

#initialize pygame library
pygame.init()

# Call methods
user_name = car.get_user_name()
car_model = car.get_car_model()
car_seating = car.get_car_seating()
max_speed = car.get_max_speed()

# Display user name with maximum speed and number of passengers
print()
console.print(f"[yellow]{user_name} is driving a {car_model} that can seat {car_seating}.[yellow]")
console.print(f"[yellow]The maximum speed of the {car_model} is {max_speed} mph.[yellow]")
print()

# TODO: User input with an exit statement
while True:

    choice = console.input(f"[bold white]Start (E)ngine | (A)ccelerate | (B)rake | (S)top  | E(x)it: [bold white]").lower()
    print()
    if choice == "e":

        # Load soundfile
        pygame.mixer.music.load('./assets/start.wav')
        # Set volume to 75%
        pygame.mixer.music.set_volume(0.75)
        # Play sound
        pygame.mixer.music.play()

        console.print(f"[bold green]The {car_model}'s engine is running.[bold green]")
        print()

    elif choice == "a":

        # Load soundfile
        pygame.mixer.music.load('./assets/acellerate.wav')
        # Set volume to 75%
        pygame.mixer.music.set_volume(0.75)
        # Play sound
        pygame.mixer.music.play()
        car.accelerate()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()

    elif choice == "b":

                # Load soundfile
        pygame.mixer.music.load('./assets/downshift.wav')
        # Set volume to 75%
        pygame.mixer.music.set_volume(0.75)
        # Play sound
        pygame.mixer.music.play()

        car.brake()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()

    elif choice == "s":

        # Load soundfile
        pygame.mixer.music.load('./assets/shutdown.wav')
        # Set volume to 75%
        pygame.mixer.music.set_volume(0.75)
        # Play sound
        pygame.mixer.music.play()

        car.stop()
        console.print(f"[bold green]The {car_model} is going {car.get_speed()} mph.[bold green]")
        print()

    elif choice == "x":
        console.print(f"[red]Thank you for visiting our dealership. Have a good day![red]")
        print()
        break



# If a standalone program, call the main function
# Else, use as a module"""
    
#if __name__ == "__main__":
    #main()