print("power calculator")
base = int(input("enter your base number"))
exponent = int(input("enter your second number"))
result = 1
for i in range(1, exponent + 1):
    result = result * base
    print("step", i, ": result =", result)
print("\nAnswer:", base, "to the power", exponent, "=", result)