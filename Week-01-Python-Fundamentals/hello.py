# this code ask user their name
name = input("what's your name? ")
# remove whitespace from str and capitalize
name = name.strip().title()
#split user name into first and last name
first, last = name.split(" ")
print ("Hello",first,last)
