class Person:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def display(self):
        return f"Customer: {self.name}, ID: {self.customer_id}"

a = Person('sanika1','006')
a = Person('sanika2','007')
a = Person('sanika3','008')
print("display: ", a.display())