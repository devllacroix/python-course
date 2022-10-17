# Excercise 0
color = "blue"
print(color)

# Excercise 1
pi = 3.14159
diameter = 3
radius = diameter / 2
area = pi * radius ** 2

print(diameter, radius, area)

# Exercise 2
a = [1, 2, 3]
b = [3, 2, 1]
print(a, b)
c = a
a = b
b = c
print(a, b)

# Excercise 3
print(5 - 3//2)
print((5-3)//2)

# Excercise 3a
print(8 - 3 * 2 - 1 + 1)
print((8 - 3) * (2 - (1 + 1)))

#Excercise 4
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your codtoe goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = -1

# Check your answer
to_smash = (alice_candies+bob_candies+carol_candies)%3
print(to_smash)

