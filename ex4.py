decimal='406.560989123'
lenth=len(decimal)
ind=0
out=''

for i in range(lenth):
    if decimal[i]=='.':
        ind=i
print(ind)
    
print(decimal[0:ind+3])

