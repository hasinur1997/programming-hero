num_one = int(input())
num_two = int(input())
num_three = int(input())

largest = 0

if num_one > num_three:
    largest = num_one
elif num_two > num_three:
    largest = num_two
else:
    largest = num_three


print(largest)