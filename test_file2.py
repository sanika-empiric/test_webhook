from person1 import Person as Employee
from person2 import Person as Customer

# Create objects of both classes
employee = Employee("John", "E12345")
employee = Employee("John1", "J12345")
customer = Customer("Alice", "C9876")
customer = Customer("Sanika", "C98769")

# Test methods from both classes
print(employee.display())  # Output: Employee: John, ID: E12345
print(customer.display())  # Output: Customer: Alice, ID: C9876
