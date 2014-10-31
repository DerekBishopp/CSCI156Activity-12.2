__author__ = 'Derek'

L = [[1,2],[1,-1],[5,8],[-4,-2],[4,3]]
M = []
for i in L:
    m = max(i)
    j = [(m, i)]
    M += j
print(sorted(M))

def mean(y):
    m = y.split(',')

    M = 0
    for i in m:
        M += int(i)
    print(M//len(m))





mean('1,2,3,4,5')



