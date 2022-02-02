# [11 , 22 , 33 , 44 , 55]
# [0     1    2    3    4]
# There are four collection data types in the Python programming language:
#
#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.
# in list we use []

num=[11,22,33,44,55]
print(num)

# print using index
print("at oth index",num[0])
print("at -3",num[-3])
print("at 1 to 3",num[1:3])
print("at 1 to present",num[1:])

# does list allows string and different data types:
name=['aman','shah',44,11.11]
print("name",name)

# does it allow duplicates
value=[11,22,11,33,44,22]
print("value",value)

# can we have list under list
name_value=[name,value]
print("name_value",name_value)

# lets try different function under list
# [11 , 22 , 33 , 44 , 55]
# [0     1    2    3    4]
num.append(44) #append will add value to last
print("num appended",num)
num.insert(1,99) #insert will insert values at index
print("num with insert",num)
num.remove(33) # it will remove value from list
print("num with remove",num)
num.pop(0)
print("num with pop 0 index",num)
num.pop() # it will pop values from last like stack
print("num with pop without index",num)
del num[2:]
print("num with del",num)
num.extend([11,22,33,44])
print("num with extend",num)
num.append([77,88]) # with append to multiple values it will create list under list in last
print("num with append",num)
num=[11,22,33,44]
#lets try min,max,sum
num_min=min(num)
print("min",min(num))
print("max",max(num))
print("max",sum(num))
num.sort
print("sort",num)
num1=[22,11,55,44]
num1.sort(reverse=True)
print("num",num1)
num1[1]=66
print("num1",num1)


a=['290 University Dr, Suite I-2', 'Madison, AL, 35806']
b=a[1].split(',')
print("b",b)
city,state=[b[0]],[b[1]]
print(city)
print(state)
# state = location[0] if len(location) > 0 else None
location = ['aman']
state = location[0] if location  else None
print(state)

