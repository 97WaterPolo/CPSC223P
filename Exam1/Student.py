# 890457906
# Alexander Sigler
# Question 2


class Student:
    def __init__(self, firstname, lastname):
        self._firstName = firstname  # Assign instance variable
        self._lastName = lastname  # Assign instance variable
        self.compareKey = '_firstName'  # Default value for compare

    def firstName(self):  # Getter function for first name
        return self._firstName

    def lastName(self):  # Getter function for last name
        return self._lastName

    def configCompKey(self, key):
        self.compareKey = key  # Assign the comparison method

    def __ge__(self, other):
        if self.compareKey in self.__dict__:  # If it exists as an attribute in dict, return it
            return self.__dict__.get(self.compareKey) >= other.__dict__.get(self.compareKey)
        else:  # Not an attribute, but a property, so get it and call it as a function
            return getattr(self, self.compareKey)() >= getattr(other, self.compareKey)()

    def __str__(self):
        return 'First Name: <' + self._firstName + '> +++ Last Name: <' + self._lastName + '>'


student = Student("Alexander", "Sigler")
student2 = Student("Bob", "Adams")

print('*** STARTING STUDENT COMPARISON OUTPUT ***')
student.configCompKey('_firstName')
print(student >= student2)  # Should Assert False
student.configCompKey('firstName')
print(student >= student2)  # Should Assert False
student.configCompKey('_lastName')
print(student >= student2)  # Should Assert True
student.configCompKey('lastName')
print(student >= student2)  # Should Assert True


