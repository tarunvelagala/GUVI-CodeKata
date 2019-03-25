try:
    n = int(input())
    if n > 0:
        lst = ['Hello'] * n
        print('\n'.join(lst))
    else:
        pass
except:
    print('invalid')
