 # Arithmetic Operators in Python.
x=81
y=27

# Addition

add_result=x+y
print(f"{x}+{y}={add_result}")

# Subtraction 

sub_result=x-y
print(f"{x}-{y}={sub_result}")

#  Multiplication 

mul_result=x*y
print(f"{x}*{y}={mul_result}")

# Division

div_result=x/y
print(f"{x}/{y}={div_result}")

#  Floor Division

fdiv_result=x//y
print(f"{x}/{y}={fdiv_result}")

#  Modulus

mod_result=x%y
print(f"{x}%{y}={mod_result}")

#  Exponentiation

exp_result=x**y
print(f"{x}**{y}={exp_result}")

# All-in-One Table (Bonus Challenge!)

print(f"""{x:<3} + {y:<3} = {add_result:<6}
{x:<3} - {y:<3} = {sub_result:<6}
{x:<3} * {y:<3} = {mul_result:<6}
{x:<3} / {y:<3} = {div_result:<6.2f}
{x:<3} / {y:<3} = {fdiv_result:<6}
{x:<3} % {y:<3} = {mod_result:<6}
{x:<2} ** {y:<3} = {exp_result:<5}""")




