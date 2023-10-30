# here are the exercises for you to practice:

# Exercise 1: Write a program to read through a file and count the number of lines. Then print the total number of lines.

# file = "words.txt"
# counts = 0
# fh = open(file)
# for lines in fh:
#     counts += 1
# print(counts)

# Exercise 2: Write a program that reads a file and prints the longest line in the file. If there are multiple lines with the same length, it should print the first one.

file = open("words.txt")
lg_line = ""
max_length = 0

for line in file:
    if len(line) > max_length:
        max_length = len(line)
        lg_line = line

print("My line: ", lg_line)


# Exercise 3: Create a program that reads a file and prints the number of words in the file.
# hf = open("words.txt")
# counts = 0
# for line in hf:
#     word = line.split()
#     counts += len(word)
# print(counts)


# Solution1:
