# Open the file containing numbers
numbers_file = open("numbers.txt", "r")
# Read the numbers from the file and split them into a list
numbers_list = numbers_file.read().split()
# Close the file
numbers_file.close()
# Create two empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []
# Loop through the numbers list and append even and odd numbers to their respective lists
# Write the even numbers to a file named "even.txt"
# Write the odd numbers to a file named "odd.txt"
# Print the output