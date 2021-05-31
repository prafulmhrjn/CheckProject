'''
3. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.
'''

stud = int(input("enter the number of students: "))
appl = int(input("enter the number of apples: "))
each = appl // stud
rem = appl - (each * stud)
print(f"the remaining numbers of apples is {rem}")
print(f"each student gets {each} ")