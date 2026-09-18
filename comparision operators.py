# comparision operators

a=10
b=20


print(a==b)
print(a !=b)
print(a>b)
print(a<b)

#age elgibility

age=int(input("enter your age:"))

print("elgibility:",age>=18)

# pass or fail checker

marks=int(input("enter your marks:"))

print("passed:", marks>=40)

#login validation

correct_username="admin"
correct_password="1234"

username=input("enter your username:")
password=input("enter your password:")

print(username==correct_username)
print(password==correct_password)

#logical operators

age=25
citizen=True
print(age>=18 and citizen==True)


has_card=False
has_cash=True

print(has_card==True or has_cash==True)

is_logged_in=True
print(not is_logged_in)

# ATM elgibility checker

balance=10000
withdraw=5000

print(withdraw>0 and withdraw<=balance)

# studen scholarship eligibility checker

marks=int(input("enter your marks:"))
attendance=int(input("enter your attendance percentage:"))

elgibility=marks>=75 and attendance>=80

print("scholarship elgibility:",elgibility)

# identity operators
a=None

print(a is None)
print(a is not None)

# bitwise operatoes 
a=5
b=3

print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)

# electricity bill calculator

units=int(input("enter the electricity units:"))

rate=6
bill=units*rate
print("electricity bill:", bill)

# travel expensive calculator

travel=float(input("travel expensive:"))
food=float(input("food expensive:"))
hotel=float(input("hotel expensive"))

total=travel+food+hotel

print("total expensive:", total)

# list in python
#list is an ordered and changeable collection that can store



# accaesing element in a list 
marks=[80,85,75,85,92]

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


