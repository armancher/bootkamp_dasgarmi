
def separator(ls):
    even_num=[]
    odd_num=[]
    for i in ls:
        if i % 2 ==0:
            even_num.append(i)
          
        else:
            odd_num.append(i)
            
    return (even_num,odd_num)
            
           
   

print(separator([1, 11, 5, 7, 3]))
print(separator([-3, -2, -1, 0, 1, 2, 3]))