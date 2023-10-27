# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = "mbox-short.txt"
fh = open(fname)
counts = dict()

for line in fh:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1
max_count = None
max_sender = None

for sender, count in counts.items():
    if max_count is None or count > max_count:
        max_sender = sender
        max_count = count
print(max_sender, max_count)

# my practices :
# fname = "mbox-short.txt"
# fh = open(fname)
# counts = dict()
# for line in fh:
#     if line.startswith("From"):
#         word = line.split()
#         sender = word[1]
#         counts[sender] = counts.get(sender, 0) + 1

# maxcount = None
# maxsender = None
# for sender, count in counts.items():
#     if maxcount is None or count > maxcount:
#         maxsender = sender
#         maxcount = count

# print(word[2])
#         count += 1
# print(word[1], count)
# if count > 1:
#     print(f"the greatest email is {count}")
# max_sender = max()
