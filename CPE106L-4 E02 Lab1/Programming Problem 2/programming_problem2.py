#Programming Problem 2:

'''
Write a program that allows the user to navigate through the lines of text in a file.
The program prompts the user for a filename and inputs the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
Actual line numbers range from 1 to the number of lines in the file.
If the input is 0, the program quits.
Otherwise, the program prints the line associated with that number 9.
'''

def main():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")
    
    try:
        # Read all lines of the file into a list
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Enter the loop to navigate through the lines
        while True:
            print(f"The file has {len(lines)} lines.")
            line_number = int(input("Enter a line number (0 to quit): "))
            
            if line_number == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_number <= len(lines):
                # Print the corresponding line
                print(lines[line_number - 1].strip())
            else:
                print("Invalid line number. Please try again.")
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
