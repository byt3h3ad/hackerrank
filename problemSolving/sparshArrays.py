# https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
    matches = []
    for i in queries:
        #print(i)
        count = 0
        for j in strings:
            if(i == j):
                count += 1
        matches.append(count)
    print(matches)
