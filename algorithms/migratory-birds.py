#https://www.hackerrank.com/challenges/migratory-birds/
def migratoryBirds(arr):
    n = len(arr)
    count = [0]*n
    for i in arr:
        count[i]+=1
    return(count.index(max(count)))
    
arr = []
print(migratoryBirds(arr))
