"""
M03 Programming Assignment - Case Study: Lists, Functions, and Classes

File Name: cdickenson_M03_CaseStudy_ListsFunctionsClasses.py
Author: Carolyn Dickenson
Updated Date: 04/02/2024
Version: 1
Purpose: This program accepts vehicle information and displays the information using a class and object.

Variables List:
vehicle_type (string) - Stores the type of vehicle. (e.g., car, truck, motorcycle, etc.) 
year         (string) - Stores the year of the vehicle.
make         (string) - Stores the make of the vehicle.
model        (string) - Stores the model of the vehicle.
doors        (string) - Stores the number of doors of the vehicle.
roof         (string) - Stores the type of roof of the vehicle.
car          (Automobile) - Stores the Automobile object.

"""
# Start of the program
# Main program ================================================================
# Display a welcome message
Welcome_Message = "\nWelcome! This program allows you to record and view details about your vehicle.\nPlease follow the prompts to enter your car's information.\n"

class Vehicle:
    def __init__(self, Vehicle_type):
        self.Vehicle_type = Vehicle_type

# Create a class named Automobile that inherits from the Vehicle class
class Automobile(Vehicle):
    def __init__(self, Vehicle_type, Year, Make, Model, Doors, Roof):
        super().__init__(Vehicle_type)
        self.Year = Year
        self.Make = Make
        self.Model = Model
        self.Doors = Doors
        self.Roof = Roof
    
    # Display the vehicle information
    def display_info(self):
        print(f"Vehicle Type: {self.Vehicle_type}")
        print(f"Year: {self.Year}")
        print(f"Make: {self.Make}")
        print(f"Model: {self.Model}")
        print(f"Doors: {self.Doors}")
        print(f"Roof: {self.Roof}")
    
def main():
    print(Welcome_Message)

    # Ask for the user for the vehicle type and accept the input or quit.
    vehicle_type = input("Enter the vehicle type (Enter 'ZZZ' to quit): ")
    if vehicle_type == 'ZZZ':
        return # Exit the program

    # loop to enter vehicle information
    while True:
        # ask for the year, make, model, number of doors, and type of roof
        year = input("Enter the year: ")
        make = input("Enter the make: ")
        model = input("Enter the model: ")
        doors = input("Enter the number of doors (2 or 4): ")
        roof = input("Enter the type of roof (solid or sun roof): ")

        print() # Print a blank line

        # Create an Automobile object
        car = Automobile(vehicle_type, year, make, model, doors, roof)

        # Display the vehicle information
        car.display_info()

        print() # Print a blank line

        # Ask if the user wants to enter another vehicle.
        choice = input("Do you want to enter another vehicle? (Enter 'ZZZ' to quit): ")
        if choice == 'ZZZ':
            break # Exit the loop

# Call the main function
if __name__ == "__main__":
    main()
