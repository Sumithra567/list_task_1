#Find the Largest Number:Given nums = [3, 7, 2, 8, 5], use a for loop to find and print the largest number.
nums = [3, 7, 2, 8, 5]
largest=0
for i in nums:
    if i>largest:
        largest=i
print("The largest number:",largest)
    