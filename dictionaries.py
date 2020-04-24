name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = []
for line in handle:
    if line.startswith("From:"):
        words = line.split()
        email = words[1]
        lst.append(email)

for add in lst:
    counts[add] = counts.get(add, 0) + 1


bigcount = None
bigemail = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = word
print(bigemail, bigcount)
