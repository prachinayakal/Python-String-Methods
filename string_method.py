# Built-In String Methods

# 1. upper()
# upper method is used to convert the text into Capital letters
text = "Welcome"
print(text.upper())

# 2. lower()
# lower method is used to convert the text into the small letters
text = "Welcome"
print(text.lower())

# 3. strip()
# strip method is used to remove the space from the beginning and the end.
text = "  Welcome to Python World   "
print(text.strip())

# 4. replace(old,new)
# replace method is used to replace old text with new text.
text = "Welcome to python world"
print(text.replace("world","Programming"))

# 5. find(sub)
# find the first occurance of a substring
text = "Hello, World!"
position = text.find("World")
print(position)                      

# 6. split(delimiter)
# Splits a string int a list based on a delimiter
text = "apple,banana,cherry"
result = text.split(",")
print(result)                               

# 7. join(list)
# Join elements of a list into a single, with an optional separator
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)                               

