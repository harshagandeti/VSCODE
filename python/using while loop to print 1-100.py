n=int(input('enter n value:'))
i=0    #i is a loop variable or starting number of print values
while i<n:
    print(i)
    i+=1


#using while loop print 1-100 in matrix form



i=1
col=10
while i<=100:
    if col>0:

        if col<100:
            print(i,end=" ")
        else:
            print(i,end=' ')
        i+=1
        col=col-1
else:
    print()
    col=10  

# add up n integer

sum=0
current=1
n=int(input('enter n value:'))
while current<=n:
    sum=sum+current
    print(sum) 




