#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#creare a tuple 
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable, see you canot add new element s
#using mergeof tuples with the + operatoryou can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#Create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#Used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index is not defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)