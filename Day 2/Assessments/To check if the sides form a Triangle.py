a = int(input(" Enter 1st side : "))
b = int(input(" Enter 2nd side : "))
c = int(input(" Enter 3rd side : "))

if a+b > c and b+c > a and c+a>b:
    print("Its a triangle")
else: 
    print("Its not a triangle")   