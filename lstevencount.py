#Count Even Numbers:Given numbers = [1, 2, 3, 4, 5, 6], use a for loop to count how many numbers are even.
numbers = [1, 2, 3, 4, 5, 6]
count=0
for i in numbers:
    if i%2==0:
        count+=1
print("Count of even numbers in given list:",count)
