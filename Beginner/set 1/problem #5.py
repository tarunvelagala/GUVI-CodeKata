try:
    m, n, o = [int(i) for i in input().split()]
    if m >= n and m >= o:
        print(m)
    elif n >= m and n >= o:
        print(n)
    else:
        print(o)
except:
    print('invalid')
