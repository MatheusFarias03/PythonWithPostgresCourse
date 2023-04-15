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

    # Here is the basic principle of destructuring.
    t = 5, 11
    x, y = t
    print(x, y)

    # Now another example.
    student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
    print(list(student_attendance.items()))

    # For each iteration, it will destructure the list into two separate variables.
    for t in student_attendance.items():
        print(t)

    people = [("Matheus", 22), ("Alice", 24)]

    for name, age in people:
        print(f"Name: {name}, Age: {age}")


# Lecture 24 - Lambda Functions.
def lambda_functions():
    
    # A lambda function is different type of function, which doesn't have a name.
    # Lambda functions are exclusively used to operate on inputs and return outputs.
    add = lambda x, y: x + y
    print(add(5, 5))

    # We can use the map() function to do an operation on each item of an array.
    sequence = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, sequence))
    print(doubled)

# Lecture 25 - Dictionary comprehensions.
def dict_comprehension():
    users = [
        (0, "Bob", "password"),
        (1, "Rolf", "rolf123"),
        (2, "Jose", "longpassword")
    ]

    username_mapping = {user[1]: user for user in users}

    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    _, username, password = username_mapping[username_input]
    
    if password_input == password:
        print("Your details are correct!")


# Lecture 26 - Unpacking arguments.
def unpack_args():

    # This function will have a set of arguments that will be collected into a
    # tuple of arguments. 
    def multiply(*args):
        print(args)
        total = 1
        for arg in args:
            total = total * arg
        return total

    print(multiply(1, 3, 5))

    # If we pass as *nums it will deconstruct the arry and add it to the respective
    # parameters.
    def add(x, y):
        return x + y

    nums = [3, 4]
    print(add(*nums))

    nums = {"x": 5, "y": 10}
    print(add(**nums))

# Lecture 28 - Object-Oriented Programming.
def OOP():
    
    class Student:
        def __init__(self, name, grades):
            self.name = name
            self.grades = grades
        
        def average(self):
            return sum(self.grades) / len(self.grades)
        
    student = Student("Bob", (90, 90, 93, 78, 84))
    print(student.name)
    print(student.average())



def main():
    OOP()
main()
