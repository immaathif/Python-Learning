year = int(input("Enter a year : "))
if ( year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("It's a Leap Year")
else:
    print("It's Not a Leap Year")
        