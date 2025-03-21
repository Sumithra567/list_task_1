#Find Words Starting with 'A':Given words = ["apple", "banana", "avocado", "grape"], use a for loop to print only the words that start with "a".
words = ["apple", "banana", "avocado", "grape"]
list=" "
for i in words:
    if i.startswith("a") or i.startswith("A"):
        list.append(i)
print(list)
