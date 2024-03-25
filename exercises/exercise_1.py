# Exercise 1
# Your solution comes here
number = int(input("Enter a number: "))

part1 = (number // 10000) + ((number // 100) % 10) + (number % 10)
part2 = ((number // 1000) % 10) + ((number // 10) % 10)
print(f"Number: {part1}{part2}")
