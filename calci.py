num1=int(input("Enter the first number="))
num2=int(input("Enter the second number="))
ch=input("Enter your arthematic choice (+,-,/,*)=")
if ch == '+':
  print(num1+num2)
elif ch == '*':
  print(num1*num2)
elif ch == '/':
  print(num1/num2)
elif ch == '-':
  print(num1-num2)
else:
  print("Invalid Operator")

