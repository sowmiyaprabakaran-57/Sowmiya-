
1.  Create a list of first 10 natural numbers. And write a program to find the lists of odd numbers and even numbers separately. And, to find the square of its odd and even lists.

# List of first 10 natural numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate odd and even numbers
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Find squares of odd and even numbers
squares_of_odd = [num ** 2 for num in odd_numbers]
squares_of_even = [num ** 2 for num in even_numbers]

print("List of odd numbers:", odd_numbers)
print("List of even numbers:", even_numbers)
print("Squares of odd numbers:", squares_of_odd)
print("Squares of even numbers:", squares_of_even)

List of odd numbers: [1, 3, 5, 7, 9]
List of even numbers: [2, 4, 6, 8, 10]
Squares of odd numbers: [1, 9, 25, 49, 81]
Squares of even numbers: [4, 16, 36, 64, 100]

2.  Write a program to find the largest and smallest number in the list without using the in-built function.

# Function to find the largest and smallest numbers in a list
def find_largest_smallest(numbers):
    if not numbers:
        return None, None  # If the list is empty, return None for both largest and smallest

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Example list of numbers
numbers = [10, 5, 8, 20, 3, 15, 7]

# Find the largest and smallest numbers
largest, smallest = find_largest_smallest(numbers)

# Print the results
print("List of numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)


List of numbers: [10, 5, 8, 20, 3, 15, 7]
Largest number: 20
Smallest number: 3

3.  Write a program to find the second largest and second smallest number in the list without using the in-built function.

# Function to find the second largest and second smallest numbers in a list
def find_second_largest_smallest(numbers):
    if len(numbers) < 2:
        return None, None  # If the list has less than 2 elements, return None for both

    # Initialize variables to store second largest and second smallest numbers
    second_largest = second_smallest = float('inf')
    largest = smallest = float('-inf')

    # Iterate through the list to find the largest and smallest numbers
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest

# Example list of numbers
numbers = [10, 5, 8, 20, 3, 15, 7]

# Find the second largest and second smallest numbers
second_largest, second_smallest = find_second_largest_smallest(numbers)

# Print the results
print("List of numbers:", numbers)
print("Second largest number:", second_largest)
print("Second smallest number:", second_smallest)

List of numbers: [10, 5, 8, 20, 3, 15, 7]
Second largest number: 15
Second smallest number: 3

4. Write a program to sort elements stored in the list as Ascending order and Descending order without using the in-built function (sort ()).                
Eg: [5,3,7,9,8,4,2]
Output: [2,3,4,5,7,8,9] – Ascending Order, 
	  [9,8,7,5,4,3,2] – Descending Order


# Function to sort elements in the list in ascending order
def sort_ascending(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

# Function to sort elements in the list in descending order
def sort_descending(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

# Example list of numbers
numbers = [5, 3, 7, 9, 8, 4, 2]

# Ascending order
sort_ascending(numbers.copy())
print("Ascending Order:", numbers)

# Descending order
sort_descending(numbers.copy())
print("Descending Order:", numbers)


Ascending Order: [5, 3, 7, 9, 8, 4, 2]
Descending Order: [5, 3, 7, 9, 8, 4, 2]

5. Find the index position of the specific number stored in the list.
Eg: a= [45,67,83,24,55,87,77,34]
What is the position of 55?
Output: 4

# Function to find the index position of a specific number in the list
def find_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1  # Return -1 if the number is not found in the list

# Example list of numbers
a = [45, 67, 83, 24, 55, 87, 77, 34]

# Number to search for
target_number = 55

# Find the index position of the target number
index = find_index(a, target_number)

# Print the result
print("Index position of", target_number, ":", index)

Index position of 55 : 4


6. Find most frequent element present in a list.
Eg: a= [4,5,6,4,6,7,4,2,4,8,4]
Output: 4

# Function to find the most frequent element in the list
def most_frequent_element(numbers):
    frequency = {}
    most_frequent = None
    max_count = 0

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        if frequency[num] > max_count:
            max_count = frequency[num]
            most_frequent = num

    return most_frequent

# Example list of numbers
a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]

# Find the most frequent element
most_frequent = most_frequent_element(a)

# Print the result
print("Most frequent element:", most_frequent)

Most frequent element: 4

7. Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value by using update method ().
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Lists
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Create an empty dictionary
result_dict = {}

# Update the dictionary with key-value pairs from the lists
for i in range(len(keys)):
    result_dict.update({keys[i]: values[i]})

# Print the resulting dictionary
print(result_dict)

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

8. Create a list of 10 members as a Voter_list. Assume that there are 3 Candidates (A, B & C) are going to contest in the election process. Write a program that voters will cast their votes and predict the Winner and Runner of the election process and to find the members who voted for the Winner and Runner.


  # List of voters
voter_list = ['Voter1', 'Voter2', 'Voter3', 'Voter4', 'Voter5', 'Voter6', 'Voter7', 'Voter8', 'Voter9', 'Voter10']

# Dictionary to store votes for each candidate
votes = {'A': 0, 'B': 0, 'C': 0}

# Voters cast their votes
for voter in voter_list:
    print(f"{voter}, please cast your vote (A, B, or C):")
    vote = input().upper()
    while vote not in ['A', 'B', 'C']:
        print("Invalid vote! Please vote again (A, B, or C):")
        vote = input().upper()
    votes[vote] += 1

# Predict the winner and runner-up
sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
winner, winner_votes = sorted_votes[0]
runner_up, runner_up_votes = sorted_votes[1]

# Find members who voted for the winner and runner-up
winner_voters = [voter for voter, vote in votes.items() if vote == winner_votes]
runner_up_voters = [voter for voter, vote in votes.items() if vote == runner_up_votes]

# Print results
print("\nElection Results:")
print(f"Winner: Candidate {winner} with {winner_votes} votes")
print(f"Runner-up: Candidate {runner_up} with {runner_up_votes} votes")
print("\nVoters who voted for the winner:", winner_voters)
print("Voters who voted for the runner-up:", runner_up_voters)

A
Voter1, please cast your vote (A, B, or C):
B
Voter2, please cast your vote (A, B, or C):
A
Voter3, please cast your vote (A, B, or C):
A
Voter4, please cast your vote (A, B, or C):
C
Voter5, please cast your vote (A, B, or C):
B
Voter6, please cast your vote (A, B, or C):
C
Voter7, please cast your vote (A, B, or C):

Invalid vote! Please vote again (A, B, or C):
B
Voter8, please cast your vote (A, B, or C):
C
Voter9, please cast your vote (A, B, or C):
A
Voter10, please cast your vote (A, B, or C):
B

Election Results:
Winner: Candidate B with 4 votes
Runner-up: Candidate A with 3 votes

Voters who voted for the winner: ['B']
Voters who voted for the runner-up: ['A', 'C']
