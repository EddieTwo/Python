# using map and lambda
celsius = [36.8, 37.3, 37.8, 39.5]
print(celsius)

fahrenheit = map(lambda x: (float(9)/5) * x + 32, celsius)
print(list(fahrenheit))

c = map(lambda x: (float(5)/9) * (x - 32), fahrenheit)
for foo in c:
    print(foo)


# filter
c1 = list(filter(lambda x: x > 37.5, celsius))
print(c1)

sm = 0
for foo in celsius: sm += foo

print(sm)

#generator
def generate_eddie():
    for v in "Eddie":
	    yield v

for foo in generate_eddie():
	print(foo, end = ' ')
print()

#emumerate
for (foo, i) in enumerate(celsius):
	print(foo, i)


# any and all
b1 = [1, 0, 0, 0]
b2 = [1, 1, 1, 1]
print(any(b1), all(b1))
print(any(b2), all(b2))
