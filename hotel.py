month=int(input())
rentpday=float(input())
ndaysst=int(input())
spmonth=[4,5,6,11,12]
if month in spmonth:
    tarrif=(rentpday+(rentpday*20/100))*ndaysst
    print("Hotel Tariff: Rs.%.2f"%tarrif)
elif month>=1 and month<=12:
        tarrif=rentpday*ndaysst
        print("Hotel Tariff: Rs.%.2f"%tarrif)
else:
    print("Invalid Input")
