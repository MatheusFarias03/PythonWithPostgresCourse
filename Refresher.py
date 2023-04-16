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

# Lecture 29 - Magic methods: __str__ and __repr__
def magic_methods():
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        # This method gets called when you want to turn your object into a string
        def __str__(self):
            return f"{self.name} is {self.age} years old"

        # The goal of this method is to be unambiguos and return a string that
        # allows us to recreate the original object.
        def __repr__(self):
            return f"<Person('{self.name}', {self.age})>"

    bob = Person("Bob", 35)
    print(bob)

# Lecture 30 - Class methods and static methods.
def class_n_static_methods():
    
    class ClassTest:
        
        # It's called an instance method because we call it on the instance.
        # An instance is an object, so these kinds of methods need to have
        # an object to be able to call them.
        def instance_method(self):
            print(f"Called instance_method of {self}")

        # With class methods, we use the 'cls' parameter instead of 'self'.
        # When we put the '@classmethod', it means that the passed argument
        # will be the class itself.
        @classmethod
        def class_method(cls):
            print(f"Called class_method of {cls}")

        # Static methods is a function inside a class which does not use it's
        # information.
        @staticmethod
        def static_method():
            print("Called static_method")


    test = ClassTest()
    test.instance_method()

    ClassTest.class_method()

    ClassTest.static_method()

    # Example on using class methods.
    class Book:
        
        # This is a class variable.
        TYPES = ("hardcover", "paperback")

        def __init__(self, name, book_type, weight):
            self.name = name
            self.book_type = book_type
            self.weight = weight
        
        def __repr__(self):
            return f"<Book '{book.name}', '{book.book_type}', {book.weight} g>"

        @classmethod
        def hardcover(cls, name, page_weight):
            return Book(name, Book.TYPES[0], (page_weight * 100 ) + 100)

        @classmethod
        def paperback(cls, name, page_weight):
            return  Book(name, Book.TYPES[1], page_weight * 100)

    book = Book.paperback("To Kill a Mockingbird", 70)

    print(book.name)


# Lecture 31 - Class inheritance.
def class_inheritance():

    class Device:

        def __init__(self, name, connected_by):
            self.name = name
            self.connected_by = connected_by 
            self.connected = True

        def __str__(self):
            return f"Device {self.name!r}, ({self.connected_by})"

        def disconnect(self):
            self.connected = False
            print("Disconnected.")

    # The 'Printer' class will inherit from the 'Device' class.
    class Printer(Device):
        
        def __init__(self, name, connected_by, capacity):
            super().__init__(name, connected_by) # Call the '__init__' method from the parent class.
            self.capacity = capacity
            self.remaining_pages = capacity

        def __str__(self):
            return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

        def print(self, pages):
            if not self.connected:
                print("Your printer is not connected!")
            else:
                print(f"Pirnting {pages} pages...")
                self.remaining_pages -= pages


    printer = Printer("Printer", "USB", 500)
    printer.print(20)
    print(printer)


# Lecture 32 - Class composition.
def class_comp():

    # Composition is a counterpart to inheritance to build classes that use
    # other classes. Composition allows classes to be simpler and reduces
    # the complexity of the code.

    class BookShelf:

        def __init__(self, *books):
            self.books = books
            self.quantity = len(self.books)

        def __str__(self):
            return f"BookShelf with {self.quantity} books"

    class Book:

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Book's title: {self.name}"

    book_lotr = Book('Lord of the Rings')
    book_got = Book('A Game of Thrones')
    shelf = BookShelf(book_lotr, book_got)
    print(shelf)


# Lecture 33 - Type hinting
def type_hinting():

    # This function is going to return a 'float' type variable
    # because of the use of '->' and also the passed argument
    # must specifically be a list.
    def list_avg(sequence: list) -> float:
        return sum(sequence)/len(sequence)

    print(list_avg([9, 7.8, 8.2]))


# Lecture 43 - Mutability
def mutability():
    
    a = []
    b = a

    # 'a' and 'b' are names. The value is the empty list '[]'.

    print(id(a))
    print(id(b))

    # The print method will return the same id because both are names
    # for the same object.

    a.append(35)

    print(a)
    print(b)

    # In python, everything is mutable because everything is an object.
    # Unless there are specifically no ways of changing the properites
    # of objects itself.

def main():
    mutability()
main()

