"""
Module 2 Case Study: If-Else and While Loops

File Name: cdickenson_M02_CaseStudy_ifelsewhile.py
Author: Carolyn Dickenson
Updated Date: 03/22/2024
Version: 1
Purpose: This program accepts student names and GPAs, and checks if the student qualifies for the Dean's List or the honor roll.

Variables List:
last_name  (string) - The last name of the student.
first_name (string) - The first name of the student.
gpa        (float)  - The GPA of the student.
"""
# Start of the program
# Main program ================================================================
# Display a welcome message
Welcome_Message = "Welcome to the Student Qualification Program!"
print(Welcome_Message)

# Goodbye message
Goodbye_Message = "Thank you for using the Student Qualification Program!"

while True:
    # Ask for the student's last name and accept the input
    last_name = input("Enter the student's last name (Enter 'ZZZ' to quit): ")
    # Check if the user wants to quit
    if last_name == 'ZZZ':
        break # Exit the loop

    # Ask for the student's first name and accept the input
    first_name = input("Enter the student's first name: ")

    # Ask for the student's GPA and accept the input
    gpa = float(input("Enter the student's GPA: "))

    # Check if the student qualifies for the Dean's List or the honor roll
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    else:
        if gpa >= 3.25:
            print(f"{first_name} {last_name} has made the honor roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or the honor roll.")
    
    print() # Print a blank line

# Display the goodbye message
print(Goodbye_Message)

# End of the program