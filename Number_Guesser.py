##### NUMBER GUESSING GAME #####
# import random
# secret_number = random.randint(1, 100)
# attempts = 0

# while True:
#    guess = int(input("Guess a number between 1 and 100: "))
#    attempts += 1

#    if guess > secret_number:
#        print("Number is too high")
#    elif guess < secret_number:
#        print("Number is too low")
#    else:
#        print("You got it!")
#        print(f"You took {attempts} attempts, great job!")
#        break

# Grade finder ig bro ###
students = ["Maurya", "Trisal", "Prabal"]
grades = [95, 96, 97]
name = input("Enter a student's name: ")
if name in students:
    students_index = students.index(name)
    students_grade = grades[students_index]
    print(f"{name}'s grade is {students_grade}")
else:
    print("Student name not found")
