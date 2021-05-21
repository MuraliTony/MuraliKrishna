num={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'};
length=[]
i=int(input("Enter a number :"))
n=i
while n != 0:
    r=n%10
    length.append(r)
    n=n//10
length.reverse()
for i in length:
    print(num[i],end=" ")
    
    """output:
    Enter a number :453
    four five three 
    Enter a number :1000
    one zero zero zero """
