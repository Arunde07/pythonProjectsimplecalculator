print(" Simple calculator ")
print(" select an option ")
print("1.Addation")
print("2.substraction")
print("3.multipliction")
print("4.division")

while" true":
    operation = int(input("enter choice(1/2/3/4)>>  "))
    num1 =float(input("enter num1>>  "))
    num2 =float(input("enter num2>>  "))

    if operation==1:
        print(num1+num2)
    elif operation==2:
         print(num1-num2)
    elif operation==3:
         print(num1*num2)
    elif operation==4:
          print(num1/num2)
    else:
        print("invalid option ! please try again")
