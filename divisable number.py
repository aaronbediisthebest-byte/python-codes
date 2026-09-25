num=int (input("enter a number(numerator): "))
print("enter a number(denominator): ")
numd=int(input())
if num%numd==5:
    print("\n"+str(num)+" is divisible by "+str(numd))
else:
    print("\n"+str(num)+" is not divisible by "+str(numd))
