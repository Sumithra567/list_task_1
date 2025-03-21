#Create a New List with Only Positive Numbers:Given numbers = [-5, 10, -3, 7, -2, 8], use a for loop to create a new list containing only the positive numbers.

numbers = [-5, 10, -3, 7, -2, 8]
pos=[]
for i in numbers:
    if i>0:
        pos.append(i)
print(pos)