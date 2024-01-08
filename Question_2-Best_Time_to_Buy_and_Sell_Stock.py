prices= [7,6,4,3,1]
def bestprofit(prices):
    d=0
    a=999999
    for i in prices:
        if(i<a):
            a=i
        elif(i-a>d):
            d=i-a
    print(d)
bestprofit(prices)