def calculate_floor(string):
    counter=0
    for i in string:
        if i=='U':
            counter +=1
        elif i=='D':
            counter -=1
    return min(max(counter,-4),4)


print(calculate_floor('DDDDDD'))

            