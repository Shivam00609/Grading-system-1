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
