name=["student1","student1","student3"]
marks=[90,87,76]
updates=[-5,6,7]
rank=[1,2,3]
new_mark=[]

l1=len(marks)
#mark updation
for a in range(l1):
    b=marks[a]+updates[a]
    new_mark.append(b)

#rank updation
l=0
    #considering stdent 1 as rank 1
if new_mark[l]>new_mark[l+1]>new_mark[l+2]: 
    rank[l]=1
    rank[l+1]=2
    rank[l+2]=3
elif new_mark[l]>new_mark[l+2]>new_mark[l+1]:
    rank[l]=1
    rank[l+1]=3
    rank[l+2]=2    
    #considering student 2 as 1st rank
elif new_mark[l+1]>new_mark[l]>new_mark[l+2]: 
    rank[l]=2
    rank[l+1]=1
    rank[l+2]=3
elif new_mark[l+1]>new_mark[l+2]>new_mark[l]:
    rank[l]=3
    rank[l+1]=1
    rank[l+2]=2    
    #considering student 3 as 1st rank
elif new_mark[l+2]>new_mark[l]>new_mark[l+1]:
    rank[l]=2
    rank[l+1]=3
    rank[l+2]=1    
elif new_mark[l+2]>new_mark[l+1]>new_mark[l]:
    rank[l]=3
    rank[l+1]=2
    rank[l+2]=1    
    
n=int(input())
if n<l1:
    print("Name:",name[n],"jump:",rank[n])
else:
    print("Index out of range")  