import re

file_name = 'input.txt'

reg = r"mul\((\d+),(\d+)\)"
res = 0
with open(file_name, 'r') as file:
    for line in file:
        matches = re.findall(reg, line)
        for match in matches:
            a, b = map(int, match)
            res += a*b
    
    print(res) 
