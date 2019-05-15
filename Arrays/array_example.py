numbers = [10, 20, 30, 40, 50, 60, 70, 2]
print(numbers[2])

#numbers[3]="Kalkulus"
print(numbers)

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

print(numbers[0:2])

##search running time is O(n)
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)


numbers.remove(20)
print(numbers)
numbers.insert(0,14)
print(numbers)