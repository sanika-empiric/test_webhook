class Person:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

a = Person('sanika','005')
print("display: ", a.display())