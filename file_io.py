# Hello World
print('Hello World!')

# Writing to a file
lst = ["Hello", "World!", "A", "message", "from", "Eddie!"]
str = ",".join(lst)
print(str)

f =  open('output.txt', 'w')
f.write(str)
f.close()

# Reading from a file
f =  open('output.txt', 'r')
str = f.read()
f.close()
lst = str.split(',')
print(lst)

# Dictionary
lst.append("Hello")
lst.append("Hello")

d = dict()
for s in lst:
	if s in d:
		d[s] += 1
	else:
		d[s] = 1

print(d)


