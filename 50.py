from time import time
start = time()
p = [2]
a = 2
def check(n):
    for i in p:
        if n%i==0:
            return False
    return True
while sum(p) < 1000000:
    a+=1
    if check(a):
        p.append(a)
i=1
while True:
    if check(sum(p[:-i])):
        print(sum(p[:-i]))
        print(time()-start)
        break
    else:
        i+=1
