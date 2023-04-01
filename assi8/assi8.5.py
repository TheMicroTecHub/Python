fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    x = line.rstrip().split()
    if 'From' not in x:
        continue

    print(x[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")