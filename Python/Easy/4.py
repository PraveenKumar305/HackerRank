n = int(input())
arr = map(int, input().split())
x = sorted(arr)
print(max([a for a in x if a != max(x)]))
