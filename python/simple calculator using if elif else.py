# simple calculator using if..,elif..,else statement

print('simple calculator')

n1=float(input('enter first value [n1]:'))
n2=float(input('enter second value [n2]:'))
operation = input('enter operation :')

# addition operation

if operation =='+':
    a=n1+n2
    print('addition [n1+n2]:',a)
    
# subtraction operation
    
elif operation =='-':
    b=n1-n2
    print('subtraction [n1-n2]:',b)
    
 # multipliction operation   
    
elif operation =='*':
    c=n1*n2
    print('multiplication [n1*n2]:',c)
    
 # division operation 
    
elif operation =='/':
    d=n1/n2
    print('division [n1/n2]:',d)
    
 # module division operation   

elif operation == '%':
     e=n1%n2
     print('module division [n1%n2]:',e)

# exponential operation

elif operation == '**':
    f = n1**n2
    print('exponential [n1**n2]:',f)
    
# invalid operation
    
else :
    print('invalid operation....:',operation)
    
