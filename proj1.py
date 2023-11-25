item=[['wal',1045,18,1],['umb',855,12,4],['cig',200,28,3],['hon',100,0,2]]
gstval=[]

for i in item:
    gst=i[1]*i[2]*.01*i[3]
    gstval.append(gst)

print('gst values',gstval)

a=[]
b=[]
for j in item:
    a.append(j[1]*j[3])

total=0
b=[a[0]+gstval[0],a[1]+gstval[1],a[2]+gstval[2],a[3]+gstval[3]]
for k in b:
    total=k

print(total)



