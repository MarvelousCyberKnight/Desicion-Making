x=int(input("Enter x "))
y=int(input("Enter y "))
z=int(input("Enter z "))
if x<y and x<z:
    print("L1 has the minimal seating capacity ")
elif y<x and y<z:
    print("L2 has the minimal seating capacity ")
else:
    print("L3 has the minimal seating capacity ")
