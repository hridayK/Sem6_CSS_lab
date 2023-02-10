val1 = int(input('Enter a number\n'))
val2 = int(input('Enter the second number\n'))

r1 = val1 # 550
r2 = val2 #15

s1 = 1
s2 = 0
t1 = 0
t2 = 1
r = -1

while(r != 0):
    q = r1//r2
    r = r1%r2
    s = s1 - (q*s2)
    t = t1 - (q*t2)

    if(r == 0):
        break
    else:
        r1=r2
        r2=r
        s1=s2
        s2=s
        t1=t2
        t2=t

    print('q\tr1\tr2\tr\ts1\ts2\ts\tt1\tt2\tt')
    print(f'{q}\t{r1}\t{r2}\t{r}\t{s1}\t{s2}\t{s}\t{t1}\t{t2}\t{t}')

ans = (val1*s2) + (val2*t2)
print(f'ans = {ans}')