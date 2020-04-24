name = input("Enter file:")
if len(name) <1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
count = dict()
for line in handle:
    if line.startswith("From"):
        splt = line.split()
        if len(splt)>2:
            hour = splt[5][:2]
            lst.append(hour)

for num in lst:
    count[num] = count.get(num, 0) + 1

lst2 = list()

for key,value in count.items():
    newtup = (key, value)
    lst2.append(newtup)
lst2 = sorted(lst2)
for key, value in lst2:
    print(key, value)
