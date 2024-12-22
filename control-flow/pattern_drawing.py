# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through rows
    row = 0
    while row < size:
        # Use a for loop to print asterisks in the current row
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1
