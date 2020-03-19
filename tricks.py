# Ternary Conditionals
print("\nTernary Conditionals:\n")
# std way
condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

# Better way
condition = True

x = 1 if condition else 0

print(x)

# Underscore Placeholders (Usefull whe you work with large numbers)
print("\nUnderscore Placeholders:\n")
# std way
num1 = 10000000000
num2 = 100000000

total = num1 + num2

print(total)

# Better way
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(total)
# to format the output
print(f'{total:,}')

# Context Managers
print("\nContext Managers:\n")
# std way
f = open('test.txt')

file_contents = f.read()

f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Better way
with open('test.txt') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# Enumerate
print("\nEnumerate Example 1:\n")
# std way
names = ["Carlos", "Andrés", "Sebastián", "Alberto"]

index = 0
for name in names:
    print(index, name)
    index += 1

# Better way (start=# is optional)
names = ["Carlos", "Andrés", "Sebastián", "Alberto"]

for index, name in enumerate(names, start=0):
    print(index, name)

# Zip:
print("\nZip: Access the same index in two groups\n")
# std way
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spyderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

for index, name in enumerate(names):
    hero = heroes[index]
    universe = universes[index]
    print(f'{name} is actually {hero} from {universe}')

# Better way
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spyderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heroes, universes):
    print(value)

# Unpacking:
print("\nUnpacking: ")
# std way
# Normal
items = (1, 2)

print(items)

# Unpacking
a, b = (1, 2)
print(a)
print(b)

a, b, *c, d = (1, 2, 3, 4, 5, 6)
print(a)
print(b)
print(c)
print(d)

# for ignore c values
a, b, *_, d = (1, 2, 3, 4, 5, 6)
print(a)
print(b)
# print(c)
print(d)

# Setattr/Getattr
print("\nSetattr/Getattr: ")


class Person():
    pass


person = Person()

person.first = "Corey"
person.last = "Schafer"

print(person.first)
print(person.last)
