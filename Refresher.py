# Lecture 8 - Getting User Input.
def sqrft_to_sqrmt():
    size_input = input("Square feet: ")
    square_feet = int(size_input)
    square_meters = square_feet / 10.8
    print(f"{square_feet} square feet is {square_meters:.2f} in square meters.")

# Lecture 9 - Writting Our First Python App.
def calculate_age():
    user_age = int(input("Type your age: "))
    months = user_age * 12
    print(f"Your age, {user_age}, is equal to {months} months.")

# Lecture 10 - Lists, tuples and sets.
def lists_tuples_sets():
    l = ["Bob", "Rolf", "Anne"] # List: Add, remove and modify elements.
    t = ("Bob", "Rolf", "Anne") # Tuple: Can't modify, add or remove elements.
    s = {"Bob", "Rolf", "Anne"} # Set: Has no duplicate elements and no order.

    print(l[0])
    l[0] = "Smith"
    l.append("Bob")
    print(l)

# Lecture 11 - Advanced set operations.
def set_operations():
    friends = {"Bob", "Rolf", "Anne"}
    abroad = {"Bob", "Anne"}

    local_friends = friends.difference(abroad)
    print(local_friends)

    students = {"Matheus", "Leonardo", "Lucas"}
    professors = {"Fabio", "Bruno"}
    college_people = professors.union(students)
    print(college_people)

    artists = {"Leonardo da Vinci", "Picasso"}
    scientists = {"Leonardo da Vinci", "Newton"}

    art_n_sci = artists.intersection(scientists)
    print(art_n_sci)

# Lecture 14 - The "in" keyword in Python.
def in_keyword():
    friends = ["Rolf", "Bob", "Jen"]
    print("Jen" in friends)

# Lecture 16 - Loops in Python.
def loops_in_py():
    grades = [7, 8, 9, 7]
    total = 0

    for grade in grades:
        total += grade
    
    print(f"Average grade : {total/len(grades)}")

# Lecture 18 - Dictionaries.
def dictionaries():
    friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
    friends_age["Bob"] = 20

    friends = [
        {"name": "Rolf", "age": 24},
        {"name": "Adam", "age": 30},
        {"name": "Anne", "age": 27},
        {"name": "Bob", "age": 20}
    ]

    for friend in friends_age:
        print(f"{friend}: {friends_age[friend]}")

    if "Anne" in friends_age:
        print(f"Anne's age: {friends_age['Anne']}")

    friends_age_value = friends_age.values()
    print(sum(friends_age_value)/len(friends_age_value))

# Lecture 19 - Destructuring Variables.
def destructuring_variables():
    pass

def main():
    dictionaries()
main()