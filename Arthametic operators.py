a=10                            # Arthamatic operators
b=3

print("addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("division:", a/b)
print("floor division:", a//b)
print("remainder:", a%b)
print("power:", a**b)




# simple calculator
a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("division:", a/b)

# students marks calculator
name=input("enter student name:")

n1=int(input("enter python marks:"))
n2=int(input("enter java marks:"))
n3=int(input("enter sql marks:"))
total=n1+n2+n3
average=total/3
print("\n----student name:", name)
print("total marks:", total)
print("average marks:", average)

# shopping bill calculator
price1=float(input("enter product 1 price:"))
price2=float(input("enter product 2 price:"))
price3=float(input("enter priduct 3 price:"))

total=price1+price2+price3

discount=total*0.10
final_amount=total-discount

print("final amount:", total)
print("discount amount:", discount)
print("final amount to be paid:", final_amount)

# SALARY CALCULATOR
basic=float(input("enter basic salary:"))

hra=basic*0.20
da=basic*0.10

gross_salary=basic+hra+da

print("basic salary:", basic)
print("hra:", hra)
print("da:", da)
print("gross salary:", gross_salary)