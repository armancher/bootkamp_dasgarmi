def find(num1, num2, num3):
    numbers={num1,num2,num3}
    for i  in range(1,5):
        if i not in numbers:
            return i
    
print(find(1,2,3))
