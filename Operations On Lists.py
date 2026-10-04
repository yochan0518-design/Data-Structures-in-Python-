#---School class Organiser---

#STEP 1- Create a list of classmates
classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev" ]
print("class list", classmates)

# STEP 2 - Access the list 
print("total students:", len(classmates))
print("first student:", classmates[0])
print("last student:", classmates[-1])
print("first three:", classmates[3])

# STEP 3 - Modify the list
classmates.append("Meera")
print("\nafter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sort Alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

# STEP 4 - Create a teacher dictionary 
teacher = {"name": "Mr.Sharma", "subject": "python", "Experience": 5}

# STEP 5 - Dictionary operators 
print("suject", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experience")
print("updated teacher profile", teacher)

# STEP 6 - convert lists into a student directory
roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Dev" ]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory )
print("Student at Roll 3:", student_directory[3])