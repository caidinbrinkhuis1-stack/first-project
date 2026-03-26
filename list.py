#Working with Lists
#List functions to add elements ==> remove(), insert()
#List functions to remove elements ==> remove(), pop()
#Other list functions sort(), reverse()
print("=========")
print("\nHello, this Program lets you stsore and display students in your class\n")
print("=========")

num_of_students = int(input("Hello, please enter the numer of students in your Class: \n"))

#create empty list
studentList = []

for y in range(0, num_of_students):
    StudentDetails = input("Enter student details; ")
    studentList.append(StudentDetails)


for x in studentList:
    print(x)
