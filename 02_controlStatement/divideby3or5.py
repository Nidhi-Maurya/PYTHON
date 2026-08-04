n = int(input("enter a number"))

if n%15==0:
    print("number is divisible by 15")
else :
    if n%5==0 | n%3==0:
     print("number is divisible by 3 and 5")
    else:
        print("number is not divisible by 3 and 5")
