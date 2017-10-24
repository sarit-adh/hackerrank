#https://www.hackerrank.com/challenges/ctci-array-left-rotation

def array_left_rotation(a, n, k):
    b = a[:]
    for i in range(0,n):
        
        
        if i-k >= 0: 
            b[i-k] = a[i]
        else: 
            b[n-(k-i)] = a[i]
    return b
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
