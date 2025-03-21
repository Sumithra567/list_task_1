#Reverse a List (Using Loop):Given words = ["hello", "world", "python"], use a for loop to print the elements in reverse order.
words = ["hello", "world", "python"]
rev=[]
for i in range(len(words)-1,-1,-1):
    rev.append(words[i])
print(rev)
