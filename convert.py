op=int(input("Enter 1(USD to INR) or 2(INR to USD): "))
if(op==1):
    num=int(input("Enter USD: "))
    print("The USD in INR is:",num*75)

elif(op==2):
    num=int(input("Enter INR: "))
    print("The USD in INR is:",num*0.013)

else:
    print("Please enter the correct number(1 or 2)!")