#For the following practice question you will need to write code in Python in the workspace below. 
# This will allow you to practice the concepts discussed in the Scripting lesson, 
# such as reading and writing files. You will see some older concepts too, but again, 
# we have them there to review and reinforce your understanding of those concepts.

#Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. 
# The main (separate) function should take user input (user's first name and last name) and 
# parse the user input to identify the first letter of the first name. 
# It should then use it to print the flower name with the same first letter (from dictionary created in the first function).

#Sample Output:

#>>> Enter your First [space] Last name only: Bill Newman
#>>> Unique flower name with the first letter: Bellflower

# Write your code here

# HINT: create a dictionary from flowers.txt
flowers_dict = {}
with open('flowers.txt') as f:
    for line in f:
        (key, value) = line.strip().split(': ')
        flowers_dict[key.lower()] = value

# HINT: create a function
        
name = input('Enter your First [space] Last name only: ')
firstLetter = name[0].lower()

print('Unique flower name with the first letter: {}'.format(flowers_dict[firstLetter]))