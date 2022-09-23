cost=float(input("Enter the price of a dozen mangoes "))
spofone=float(input("Enter the price at which 1 mango is being sold "))
sp=spofone*12
if sp>cost:
    profit=sp-cost
    print("Profit : Rs.%.2f" %profit)
elif sp==cost:
    print("No profit nor loss")
else:
    loss=cost-sp
    print("Loss : Rs.%.2f" %loss)
