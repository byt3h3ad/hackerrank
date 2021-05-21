#https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    return sum([ar.count(i)//2 for i in set(ar)])
  
from collections import Counter
input()
socks, pairs = Counter(map(int,input().strip().split())), 0
for s in socks: pairs += socks[s]//2
print(pairs)

input()
socks = input().strip().split()
pairs = 0

for element in set(socks):
	pairs += socks.count(element) // 2
print(pairs)
