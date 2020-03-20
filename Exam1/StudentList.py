# 890457906
# Alexander Sigler
# Question 3
from Student import Student  # Import our other student object for typing


class StudentList(list):  # Specify it inherits the native object of list
    lastNameDictionary = {}  # Empty dict to hold our last name sorting

    def insert(self, index: int, newstudent: Student):
        super().insert(index, newstudent)  # Call original insert

        # Check if the last name already exisits in the dictionary
        if newstudent.lastName() not in self.lastNameDictionary:
            self.lastNameDictionary[newstudent.lastName()] = []  # Create a new list for that last name
        self.lastNameDictionary.get(newstudent.lastName()).append(newstudent)  # Insert the new student

    def __getitem__(self, key):
        # If an int, use the normal index, otherwise return last name based on string
        return super().__getitem__(key) if isinstance(key, int) else self.lastNameDictionary[key]


s1 = Student("Alexander", "Sigler")
s2 = Student("Bob", "Sigler")
s3 = Student("Joe", "Smith")
s4 = Student("George", "Wiler")


sList = StudentList()

sList.insert(0, s1)
sList.insert(0, s2)
sList.insert(0, s3)
sList.insert(1, s4)
print('*** STARTING STUDENT LIST OUTPUT ***')
print('\nThe first value in the list:')
print(sList[0])
print('\nThe last value in the list:')
print(sList[len(sList)-1])
print('\nThe names with last name Sigler')
for x in sList['Sigler']:
    print(x)
print('\nThe names with last name Smith')
for x in sList['Smith']:
    print(x)






