"""
Question 087 - Level 03
By using list comprehension, please write a program to print the list after removing the value 24 in
[12,24,35,24,88,120,155].
Hints: Use list's remove method to delete value.
--- Nguyen Van Duc ---
"""
li = [12, 24, 35, 24, 88, 120, 155]
li = [x for x in li if x != 24]
print(li)
