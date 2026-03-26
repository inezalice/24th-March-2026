# # Online exam qualification
# registered = input("Are you registered: yes/no")
# tuition_fee = input("Are the tuition fee paid:")

# if tuition_fee == "yes" and registered == "yes":
#     print("Cleared for the exam")
# elif tuition_fee == "no" and registered == "yes":
#      print("Not allowed for exam")
# else:
#     print("You are nor allowed to come to school")

    
#  # Cheking a number
# number = int(input("Enter a number:"))

# if number > 0:
#     print("The number is positive")
# elif number < 0:
#      print("The number is negtive")
# else:
#     print("The number is neutral")  


# # Grading system simulation
# Grade = float(input("Enter your grades: "))
# if Grade > 80:
#     print("You are in grade A")
# elif Grade >= 70:
#     print("You are in grade B")
# elif Grade >= 60:
#     print("You are in grade C")
# elif Grade >= 50:
#     print("You are in grade D")
# else:
#     print("You failed") 

# Salary increment based on experince
salary = int(input("Your actual salary:"))
Experience = int(input("Enter your years of experience:"))

if Experience >= 10:
    Newsalary = salary + (salary * 0.005)
    print("Your new salary is:", Newsalary)
    
elif Experience >= 5:
    Newsalary = salary + (salary * 0.002)
    print("Your new salary is:", Newsalary)
    
else:
    print("work hard")

   
