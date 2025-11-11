# Grading-system-1
Grade Calculator Program (Python)

This Python program takes a student's marks as input and determines their grade based on the following criteria:

Marks Range	Grade
90 and above	A+
80 to 89	A
75 to 79	B+
70 to 74	B
50 to 69	C
35 to 49	D
Below 35	Fail
How the Program Works

The user is prompted to enter their marks.

The program evaluates the input using if, elif, and else conditions.

The corresponding grade is displayed.

Python Code
Marks=int(input("Enter marks : "))
if Marks>=90:
    print("grade : A+")
elif Marks>=80 and Marks<90:
    print("grade = A")
elif Marks>=75 and Marks<80:
    print("grade = B+")
elif Marks>=70 and Marks<75:
    print("grade = B")
elif Marks>=50 and Marks<70:
    print("grade = C")
elif Marks>=35 and Marks<50:
    print("grade = D")
else:
    print("You are fail")

Example Output
Enter marks : 82
grade = A

Usage

Make sure you have Python installed.

Run the program using:

python filename.py
