'''Task 1: Dictionary, Set, and Tuple

    choose the best data structure for each cenario, then imlplement that structure in Python.'''


# 1. Store the months of the year as strings. Determine the month in the data structure in which Pi Day exists and print that month to the console. 


months = {
    1: "Jauary", 
    2: "February",
    3: "March",
    4: "April", 
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def get_first_digit():
    pi_day = 3.14
    int_pi_day = int(pi_day)
    return int_pi_day

def find_pi_day(int_pi):
    result = print(months[int_pi])
    return (result)

def pi_day():
    int_pi_day = get_first_digit()
    find_pi_day(int_pi_day)




# 2. Store 5 fruits or veg. Add two of your fav fruits and two veg to the collection. Itrate over the collction and print each one to the console. 

def produce():

    fav_produce = {"apples", "oranges", "apricots", "broccoli_rabe", "pinapple"}
    new_produce = ["mango", "coconut", "asparagus", "cauliflower"]
    fav_produce.update(new_produce)
    print(fav_produce)


#3: Store info about a user profile. Use literal string interpolation to print the profile info to the console. 

def store_profile():

    user_profile = {
        "First Name" : "Emily",
        "Last Name" : "Twines",
        "Email Address": "some@email.com",
        "Phone Number": "(123) 456 - 7890"
    }
    a = user_profile['First Name']
    b = user_profile["Last Name"]
    c = user_profile["Email Address"]
    d = user_profile["Phone Number"]
    print(f"My user's name is {a} {b}, their email is {c}, and their phone number is {d}.".format(a, b, c, d))



'''
Task 2: List of Dictionaries
    use a list to store the dict of you immediate family, with each index of the list storing its own dict. dict should contain: 
    first name, last name, relation to you.
    Write a function that will iterate over the list and print the first name and relation of each person.'''


sarah = {
"First Name": "Sarah",
"Last Name": "Winters",
"Relation": "Mother"
}

jacky = {
"First Name": "Jacky",
"Last Name": "Winters",
"Relation": "Step-Father"
}

ian = {
"First Name": "Ian",
"Last Name": "Delbridge",
"Relation": "Brother"
}


family = [sarah, jacky, ian]

def first_and_relation():
    index = 0
    while index < len(family):
        # print(family[index])
        for key, value in family[index].items():
            result = family[index].get("First Name")
            result1 = family[index].get("Relation")
            print(f"{result} is my {result1}.")
            index += 1
        
    


