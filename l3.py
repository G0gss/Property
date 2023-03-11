class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):

        return self._age

    def set_age(self, age):
        self._age = age
    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender


person = Person("Jana", 25, "female")
print(person._name)
print(person._age)
print(person._gender)