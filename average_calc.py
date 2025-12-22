# Average Calculator
# Created by: Shem
# Created on: 2025/12/09
# This program generates random numbers and calculates the average
# Copyright 2025 Shem
import random


# Main function that controls program flow
def main():
    # Initialize variables
    # total sum of numbers
    total = 0
    # list to store numbers
    num_list = []
    num_min = 0
    num_max = 100
    max_number_of_num = 10
    # Loop to generate numbers
    for loop_counter in range(0, max_number_of_num):
        # Generate a random number
        rand_num = random.randint(num_min, num_max)
        # Add number to list
        num_list.append(rand_num)
        # Add number to total sum
        total += rand_num
        # Print each number as it's added (without f-string)
        print(str(rand_num) + " has been added to the sum.")
    # Calculate the average
    average = total / max_number_of_num
    # Print the list of numbers
    print("\nRandom Numbers:", num_list)
    # Print the average (without f-string)
    print("Average: " + str(average))
    # Thank you message
    print("Thank you for using the program")
    print(" /\\_/\\  ")
    print("( ^_^ )")
    print(" > ^ < ")

# Start the program
if __name__ == "__main__":
    main()
