#Programming Problem 2:

'''
Write a program that allows the user to navigate through the lines of text in a file.
The program prompts the user for a filename and inputs the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
Actual line numbers range from 1 to the number of lines in the file.
If the input is 0, the program quits.
Otherwise, the program prints the line associated with that number 9.
'''

'''
Note for Users:
When being prompted for the name of the file, do not forget to add the filename extension!
The program will not work if you just simply input "text" as a file, you must write "text.txt"!

Just a heads up!
:)
'''

filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    while True:
        print(f"The file has {len(lines)} lines.")
        line_number = int(input("Enter a line number (0 to quit): "))
        if line_number == 0:
            print("Exiting the program.")
            break
        elif 1 <= line_number <= len(lines):
            print(lines[line_number - 1].strip())
        else:
            print("Invalid line number. Please try again.")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")

