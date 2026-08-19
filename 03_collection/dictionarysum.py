input = {"a":100, "b":200, "c":300}

sum=0

for x in input.items():
    sum+=x[1]
print(sum)