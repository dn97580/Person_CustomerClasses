# Project #2: Person and Customer Classes
# Write a class named Person with data attributes for a person's name, address,
# and telephone number. Next, write a class named Customer that is a subclass of
# the Person class. The Customer class should have a data attribute for a customer 
# number, and a Boolean data attribute indicating whether the customer wishes to
# be on a mailing list. Demonstrate an instance of the Customer class in a simple 
# program.

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

        # create a Customer object
customer = Customer("John Doe", "123 Main St.", "555-1234", "12345", True)

# print the object's attributes
print("Name:", customer.name)
print("Address:", customer.address)
print("Phone:", customer.phone)
print("Customer Number:", customer.customer_number)
print("Mailing List:", customer.mailing_list)
