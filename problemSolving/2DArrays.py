# https://www.hackerrank.com/challenges/2d-array/

def hourglassSum(arr):
    sum = 0
    big = float('-inf') 
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if (big < sum):
                big = sum
    print(big)
