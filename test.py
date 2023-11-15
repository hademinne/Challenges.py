# mylist =list()
# mylist.append('book')
# mylist.append(100)
# print(mylist)


# me = 'Hademinne';
# me = me.lower()
# print(me)


# me1= ['h','a','d','e','m','i','n','n','e']
# 'x' in me1
# print(me1[3:7])
# # for letter in me1:
# #   print('letter: ', letter)


# t = [1,5,6,7,9,0]
# print(t[1:3])

# mylist1 ='this,is,first,try'
# test = mylist1.split(',')
# print(test)

# for w in mylist1:
#   print(w)

# print(test[2])


# line ='this my email: hademinne@gmail.com'
# adress=line.split()

# email=adress[3]

# pieces=email.split('@')

# print(pieces[0])

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(len(c))

# mydic = dict()
# mydic["hadminne"] = "officer"
# print(mydic)


counts = dict()
names = {"valla", "nana", "nana", "nevisa", "nana"}
# for name in names:
#     if name not in counts:
#         counts[name] = 1

#     else:
#         counts[name] = counts[name] + 1

print(counts.keys())


# # counting pattern:
# counts = dict()
# print("enter a line or text:")
# line = input("")

# words = line.split()
# print("words:", words)

# print("counting...")
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("counts", counts)


# stuff = dict()
# print(stuff.get("candy", -1))
# y = (1, 8, 5)

# y[1] = 3
# print(y)

# book = dict()
# book["dev"] = 5
# book["cyber"] = 3
# for k, v in book.items():
#     print(k, v)
# tups = list(book.items())
# print(tups)
# print(tups[1])

# d = {"a": 10, "b": 1, "c": 22}
# t = sorted(d.items())
# print(t)
# for k, v in sorted(d.items()):
#     print(k, v)

# sort by values instead of key:
# d = {"a": 10, "b": 1, "c": 22}
# tmp = list()
# for k, v in d.items():
#     tmp.append((v, k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)
#


# /////////////////
# Overall, the code reads a file, counts the occurrences of each word, stores the results in a list of tuples, sorts the list in descending order by count, and then prints the top 10 most frequent words along with their counts.

# fhand = open("romeo.txt")
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
#     print(lst)
# lst = sorted(lst, reverse=True)

# for val, key in lst[:10]:
#     print(key, val)

# //////////////////
# Matching and Extracting Data
# import re

# x = "My 2 favorite numbers are 12 and 20"
# y = re.findall("[0-9]+", x)
# print(y)

# x = "From: Using the : character"
# y = re.findall("^F.+:", x)
# print(y)

# //////////////////////
# week 5  JavaScript Object Notation (JSON)
import json

input_data = """[
    {"id": "001", "x": "2", "name": "hademinne"},
    {"id": "009", "x": "7", "name": "hademinne"}
]"""

# Remove newline characters from the string
input_data = input_data.replace("\n", "")

info = json.loads(input_data)
print("User count:", len(info))
for item in info:
    print("Name:", item["name"])
    print("Id:", item["id"])
    print("Attribute:", item["x"])
