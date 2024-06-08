

names = ['Claive','Rolando', 'De','Sousa','Monteza']

# print all list
print(names)

# First name on the list
print(names[0])

# Last name on the list
print(names[-1])

# replace a name on the index
names[-1] = 'Vallejos'
print(names)

# Range values
print(names[0:4])


#LIST METHODS
##Insert method
names.insert(5,'Oliver')
print(names)

##Remove Method
names.remove("Oliver")
print(names)

## remover all items
names.clear()
print(names)


## check is a item existe on list
print('Oliver' in names)

## return a number of item in a list
print(len(names))

