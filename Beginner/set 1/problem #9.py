try:
    n, k = [int(i) for i in input().split()]
    lst = [int(i) for i in input().split()]
    print(sum([lst[j] for j in range(k)]))
except:
    print('invalid')
