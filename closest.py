n = int(input())
m = int(input())
mindiff = float('inf')
closest =0
for i in range(n - abs(m), n + abs(m)):
    if i%m == 0:
       diff = abs(n - i)

       if(mindiff > diff):
        mindiff = diff
        closest = i
       elif(mindiff == diff) and abs(i) > abs(closest):
        closest = i
      
print(closest)
