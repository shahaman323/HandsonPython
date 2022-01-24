#variable is a container where we put our value

x=5
print(x)
print(x+3)
# we can modify the variables value
x=9
print(x)
y=10
print(y)
print(x+10)
# what if i want to add value to previous value
# print(19+10) or use below
# print(_)

# variables with strings
name='aman'
print(name)
print(name+' shah')
# fetch variables character
print(name[0])
print(name[1])
print(name[-1])

# what if u want to put index
# a m a n
# 0 1 2 3
print(name[0:2])
print(name[1:3])
# what if i mention only starting index
# it will print till starting index to ending index
print(name[1:])

# what if i mention only ending index
print(name[:2])

# what if i print ending index out of range
# it will print till available, wont throw error
print(name[:10])
# string in python is immutable
# print(name[0]='s')
change_name='s' + name[1:3]
print(change_name)

# count the length
my_name='aman shah'
print(len(my_name))