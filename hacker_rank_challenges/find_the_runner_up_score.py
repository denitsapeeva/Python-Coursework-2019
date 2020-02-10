from pip._vendor.distlib.compat import raw_input
if __name__ == '__main__':
 n = int(raw_input())
 arr = map(int, raw_input().split())
a = max(arr)
for x in range(len(arr)-1, -1, -1):
            if arr[x] == a:
             arr.remove(arr[x])
print(max(arr))
