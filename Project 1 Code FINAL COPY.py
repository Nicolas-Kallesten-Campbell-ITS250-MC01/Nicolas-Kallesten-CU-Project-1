# This is the percent breakdown of the course
QUIZ_PERCENTAGE = .3
PRO_HW_PERCENTAGE = .3
MIDTERM_PERCENTAGE = .2
FINAL_EXAM_PERCENTAGE = .2



# Here is where you will enter specific quiz grades
quiz_1 = int(input("Enter your grade for Quiz 1: "))

if quiz_1 >= 0 and quiz_1 <= 100:
    quiz_1 == quiz_1
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_2 = int(input("Enter your grade for Quiz 2: "))

if quiz_2 >= 0 and quiz_2 <= 100:
    quiz_2 == quiz_2
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_3 = int(input("Enter your grade for Quiz 3: "))

if quiz_3 >= 0 and quiz_3 <= 100:
    quiz_3 == quiz_3
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_4 = int(input("Enter your grade for Quiz 4: "))

if quiz_4 >= 0 and quiz_4 <= 100:
    quiz_4 == quiz_4
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_5 = int(input("Enter your grade for Quiz 5: "))

if quiz_5 >= 0 and quiz_5 <= 100:
    quiz_5 == quiz_5
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_6 = int(input("Enter your grade for Quiz 6: "))

if quiz_6 >= 0 and quiz_6 <= 100:
    quiz_6 == quiz_6
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_7 = int(input("Enter your grade for Quiz 7: "))

if quiz_7 >= 0 and quiz_7 <= 100:
    quiz_7 == quiz_7
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_8 = int(input("Enter your grade for Quiz 8: "))

if quiz_8 >= 0 and quiz_8 <= 100:
    quiz_8 == quiz_8
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_9 = int(input("Enter your grade for Quiz 9: "))

if quiz_9 >= 0 and quiz_9 <= 100:
    quiz_9 == quiz_9
else:
    print("Please input a number between 0 and 100.")
    quit()


quiz_10 = int(input("Enter your grade for Quiz 10: "))

if quiz_10 >= 0 and quiz_10 <= 100:
    quiz_10 == quiz_10
else:
    print("Please input a number between 0 and 100.")
    quit()


# Here you will get the overall quiz averages
quiz_avg = (quiz_1 + quiz_2 + quiz_3 + quiz_4 + quiz_5 + quiz_6 + quiz_7 + quiz_8 + quiz_9 + quiz_10) / 10

print("Your overall quiz average is:", quiz_avg)



print()



# Here is where you input the grade for the MyProgrammingLab
mpl_grade = int(input("Please input your MyProgrammingLab average: "))

if mpl_grade >= 0 and mpl_grade <= 100:
    mpl_grade == mpl_grade
else:
    print("Please input a number between 0 and 100.")
    quit()

# Here is where you will put in the grade for project 1
project_1 = int(input("Please input your Project 1 Grade: "))

if project_1 >= 0 and project_1 <= 100:
    project_1 == project_1
else:
    print("Please input a number between 0 and 100.")
    quit()

# Here is where you will input the grade for project 2
project_2 = int(input("Please input your Project 2 Grade: "))

if project_2 >= 0 and project_2 <= 100:
    project_2 == project_2
else:
    print("Please input a number between 0 and 100.")
    quit()

# Here is where you will input grade for project 3
project_3 = int(input("Please input your Project 3 Grade: "))

if project_3 >= 0 and project_3 <= 100:
    project_3 == project_3
else:
    print("Please input a number between 0 and 100.")
    quit()


# Here is where you get your overall MyProgrammingLab average
pro_hw_avg = (mpl_grade + project_1 + project_2 + project_3) / 4

print("Your overall homework/project average is:", pro_hw_avg)



print()


# Here is where you will enter student's midterm grade
midterm_grade = int(input("Enter your midterm exam grade: "))

if midterm_grade >= 0 and midterm_grade <= 100:
    midterm_grade == midterm_grade
else:
    print("Please input a number between 0 and 100.")
    quit()


print()


# Here is where you enter the student's final exam grade
final_exam_grade = int(input("Enter your final exam grade: "))

if final_exam_grade >= 0 and final_exam_grade <= 100:
    final_exam_grade == final_exam_grade
else:
    print("Please input a number between 0 and 100.")
    quit()


print()


# Here is where you breakdown all of the averages to get the students final grade
final_grade = (quiz_avg * QUIZ_PERCENTAGE) + (pro_hw_avg * PRO_HW_PERCENTAGE) + (midterm_grade * MIDTERM_PERCENTAGE) + (final_exam_grade * FINAL_EXAM_PERCENTAGE)

print("Your final grade in ITS250 is:", final_grade)

while final_grade < 60:
    print("Sorry, you failed the class! You got an F :(")
    final_grade == final_grade
    break

while final_grade >= 60 and final_grade < 70:
    print("You finished the class with a D.")
    final_grade == final_grade
    break

while final_grade >= 70 and final_grade < 80:
    print("YOu finished the class with a C. Not bad!")
    final_grade == final_grade
    break

while final_grade >= 80 and final_grade < 90:
    print("You finished the class with a B. Good work!")
    final_grade == final_grade
    break

while final_grade >= 90 and final_grade <= 100:
    print("You finished the class with an A. Awesome job!")
    final_grade == final_grade
    break
