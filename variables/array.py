array = [15, 5, 63, 52, 11, "Rodrigo"]
array2 = [45, 69, 22, 2, 63, 4]
print(array)

# print(array[5])
# print(array[1:4])
# print(array[:2])
# print(array[3:])
# array[0] = "Alex"
# print(array)

# The append() method is used to add an element to the end of a list. It modifies the original list by adding the specified element as its last item. 
print("Before append():", array)
array.append("Doug")
print("After append():", array)

# The index() method in Python is used to find the index of the first occurrence of a specified value within a list.
index = array.index("Doug")
print(index)

# The insert() method in Python is used to insert an element into a list at a specified index.
print("Before insert():", array)
array.insert(3, "Amanda")
print("After insert():", array)

# The pop() method in Python is used to remove and return the last element from a list, or an element at a specified index. 
print("Before pop():", array)
array.pop(4)
print("After pop():", array)

# The remove() method in Python is used to remove the first occurrence of a specified value from a list.
print("Before remove():", array)
array.remove("Rodrigo")
print("After remove():", array)

# The sort() method in Python is used to sort the elements of a list in ascending order.
print("Before sort():", array2)
array2.sort()
print("After sort():", array2)
