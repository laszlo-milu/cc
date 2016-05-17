doors=[]
doors=doors+[0]*100
for i in range(1,101):#checks doors from 1 to 100
   for j in range(1,101):#with numbers 1 to 100
       if (i%j==0):#if number "j" is multiplier of "i"
           doors[i-1]+=1
for i in range(100):
    if (doors[i]%2==1):#if "i" number is odd
        print(i+1)
