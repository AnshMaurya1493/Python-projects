l=[1,2,3,4,5,6,7,8,9,10]
new=[]
count=0
print(count)
def even_and_count():
    
    for i in l:
        if i%2==0:
            new.append(i)
            global count
            count=count+1    
    print("Even Numbers in list:",new,end="")
    print(" no of element: ",count)        
def odd_and_count():
    
    for i in l:
        if i%2 !=0:
            new.append(i)
            global count
            count=count+1    
    print("odd Numbers in list:",new,end="")
    print(" no of element: ",count)
even_and_count();
odd_and_count();
