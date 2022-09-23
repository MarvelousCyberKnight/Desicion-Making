byear=int(input("Enter year of birth "))
cyear=int(input("Enter current year "))
if cyear>byear:
    age=cyear-byear
    print("Your age is %d"%age)
else:
    age=cyear-byear+100
    print("Your age is %d"%age)
