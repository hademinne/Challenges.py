import re

# Read the data file
file_name = ".txt"  # Update this with your file name
with open(file_name, "r") as file:
    data = file.read()

# Find all the numbers in the text
numbers = re.findall("[0-9]+", data)

# Convert the extracted strings to integers and sum up the integers
total_sum = sum(int(number) for number in numbers)

# Print the total sum
print("Sum:", total_sum)
