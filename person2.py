class Person:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def display(self):
        return f"Customer: {self.name}, ID: {self.customer_id}"

a = Person('sanika1','006')
b = Person('sanika2','007')
c = Person('sanika3','008')
d = Person('sanika4','009')
e = Person('sanika5','0010')
print("display: ", a.display())