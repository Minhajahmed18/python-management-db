'''
for i in range(0,6):
    print(i)
'''


## Check logic of Element Delering from List

list_temp=[1,2,3,4,5,6]
j=2
k=0
copied_list=[]
for i in range(0,len(list_temp)):
   if(j==i):
       continue
   else:
       copied_list.append(list_temp[i])
       k=k+1

print(copied_list)
