class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender


person = Person("Jana", 25, "female")
print(person.name)
print(person.age)
print(person.gender)

print("---------------------------------")
person.name = "Steve"
person.age = 30
person.gender = "male"
print(person.name)
print(person.age)
print(person.gender)
