sentence = "You learn more from failure than from success."

# Extracting the characters
first_char = sentence[0]  # 'Y'
fourth_char = sentence[3]  # 'l'
last_char = sentence[-1]    # '.'

# Creating the new string
new_string = first_char + fourth_char + last_char
print(new_string)  # Output: Yl.


# Replacing "." with "!"
new_sentence = sentence.replace(".", "!")
print(new_sentence)  # Output: You learn more from failure than from success!

# Creating a new variable with all lowercase characters
lowercase_sentence = sentence.lower()
print(lowercase_sentence)  # Output: you learn more from failure than from success.

# Creating a new variable with all uppercase characters
uppercase_sentence = lowercase_sentence.upper()
print(uppercase_sentence)  # Output: YOU LEARN MORE FROM FAILURE THAN FROM SUCCESS.


# Checking if the string starts with "Z"
starts_with_Z = sentence.startswith("Z")
print("Starts with 'Z':", starts_with_Z)  # Output: False

# Checking if the string starts with "t"
starts_with_t = sentence.startswith("t")
print("Starts with 't':", starts_with_t)  # Output: False

lowercase_sentence = "you learn more from failure than from success."

try:
    index_of_j = lowercase_sentence.index("j")
    print("Index of 'j':", index_of_j)
except ValueError:
    print("Character 'j' not found in the string.")

lowercase_sentence = "you learn more from failure than from success."

# Counting occurrences of "t" and "o"
count_t = lowercase_sentence.count("t")
count_o = lowercase_sentence.count("o")

# Creating a print statement with both results
print(f"The character 't' appears {count_t} times and the character 'o' appears {count_o} times.")

# Finding the length of the string
length_of_sentence = len(sentence)
print("Length of the string:", length_of_sentence)


# Checking if all characters are alphabetic
all_alpha = sentence.replace(" ", "").isalpha()  # Removing spaces for the check
print("All characters are alphabetic:", all_alpha)

# Using find() method
find_y = sentence.find("y")
print("Using find():", find_y)

# Using index() method
try:
    index_y = sentence.index("y")
    print("Using index():", index_y)
except ValueError:
    print("Character 'y' not found using index()")

# Difference between find() and index()
# The find() method returns the lowest index of the substring if found, 
# or -1 if the substring is not found. The index() method also returns 
# the lowest index, but it raises a ValueError if the substring is not found.

# Initialize a dictionary to hold character counts
char_count = {}

# Count each character in the string
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"'{char}': {count}")