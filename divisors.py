li=[]
def divi(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i,end=" ")
            
num=int(input('enter the no'))
print('divisors of ',num,'are')
divi(num)
