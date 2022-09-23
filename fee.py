student=input("Enter the student type\n")
a=["MSH","MSDS","MGSDS","MGSH"]
if a[0] == student:
    n1=float(input("Enter tuition fee\n "))
    n2=float(input("Enter hostel fee\n "))
    n3=n1+n2
    print("The fees to be paid by the student is Rs.%.2f "%n3)
elif a[1] == student:
    n1=float(input("Enter tuition fee\n ")) 
    n2=float(input("Enter bus fee\n "))
    n3=n1+n2
    print("The fees to be paid by the student is Rs.%.2f "%n3) 
elif a[2] == student:
    n1=float(input("Enter tuition fee\n "))
    n2=float(input("Enter bus fee\n "))
    n3=n1*150/100
    n4=n3+n2
    print("The fees to be paid by the student is Rs.%.2f "%n4)
elif a[3] == student:
    n1=float(input("Enter tuition fee\n "))
    n2=float(input("Enter hostel fee\n "))
    n3=n1*150/100
    n4=n3+n2
    print("The fees to be paid by the student is  Rs.%.2f "%n4)
