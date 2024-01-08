s=[5,1,6]

def subsets(arr):
    x = len(arr)
    l=[]
    for i in range(1 << x):
        l.append([s[j] for j in range(x) if (i & (1 << j))])
    return l
    
def xorsum(l):
    k=0
    for i in l:
        a=0
        for j in i:
            a^=j
        k+=a
    print(k)
    
xorsum(subsets(s))