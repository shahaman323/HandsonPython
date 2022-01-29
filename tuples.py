# There are four collection data types in the Python programming language:
#
#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.

# tuple is opposite of list
# In tuple we use ()

# lets create a tuple first
tup = (22, 11, 44, 55)
print(tup)
print(type(tup))

# main difference is tuples is immutable, lets check it
# tup[1]=33
# above code shows error


# since we dont change values in tuples
# so iteration in tuples is faster than list

# lets try some operations in tuples
# count occurence of a value
print(tup.count(22))

# fetch the index of a value
print(tup.index(22))


