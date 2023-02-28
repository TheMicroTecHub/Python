import re
fhand = open('regex_sum_1736017.txt')
num = 0
for line in fhand:
    line = line.strip()
    x = re.findall('[0-9]+',line)
    for z in x:
        num = num + int(z)
print(num)