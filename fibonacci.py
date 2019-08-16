n=int(input('enter the no of ele'))
count=0
#sum=0
a=0
b=1

li=[]
li.append(a)
li.append(b)
while count<n-2:
    summ=a+b
    li.append(summ)
    a=b
    b=summ
    count+=1
print('the fibonacci nos are')    
print(li)    
