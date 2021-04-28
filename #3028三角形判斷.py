a = int(input())
b = int(input())
c = int(input())

if a>= b and a>=c:
    if a >= b+c:
        print("False")
        
    else:
        print("True")
        if c*c + b*b==a*a:
            print("Right Triangle")
        else:
            print("Non-Right Triangle")

elif b>= a and b>=c:
    if b >= a+c:
        print("False")
        
    else:
        print("True")
        if a*a + c*c == b*b:
            print("Right Triangle")
        else:
            print("Non-Right Triangle")

else:
    if c >= b+a:
        print("False")
        
    else:
        print("True")
        if a*a + b*b == c*c:
            print("Right Triangle")
        else:
            print("Non-Right Triangle")
