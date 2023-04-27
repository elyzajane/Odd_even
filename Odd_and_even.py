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
for number in numbers_list:
    if int(number) % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
# Write the even numbers to a file named "even.txt"
even_file = open("even.txt", "w")
for number in even_numbers:
    even_file.write(number + "\n")
even_file.close()
# Write the odd numbers to a file named "odd.txt"
odd_file = open("odd.txt", "w")
for number in odd_numbers:
    odd_file.write(number + "\n")
odd_file.close()
# Print the output