# student management system
# Input multiple students
# Store their marks
# Compute average


class Student:
    def __init__(self , name ,marks):
        self.name = name
        self.marks=marks
        print("hi", {name}, "welcome")
    def get_average(self):
        return sum (self.marks)/len(self.marks)
    def get_result(self):
        avg =self.get_average()
        return "pass" if avg >=40 else "fail"
    # to append marks and name in list 
students=[]

n= int(input("enter the number of student:"))
for i in range(n):
        name= input(f"enter the name of student:")
        marks = list(map(int, input(f"Enter the marks for student {i+1} (separated by spaces): ").split()))
        s= Student(name, marks)
        students.append(s)
        #ab now to print them when called
print("\n ---results---")
for s in students:
        
        avg = s.get_average()
        results = s.get_result()
        print(f"  Name:{s.name}")
        print(f" Average:{avg:.2f}")
        print(f" Result :{results}")


