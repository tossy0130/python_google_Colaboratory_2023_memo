import random
key = random.randint(1, 10)
print(str(key))

### ========= 線形探査 =========
def get_line(arr):
  for i in range(0, len(arr)):
    if key == arr[i]:
      return key
  return None

t_list = [1,2,5,8,10]

print("\n" + "=== 線形探査（出力） ===")
print(get_line(t_list))
print("======" + "\n")

### ==========　二分探索 =========
def binary_search(arr):
  left = 0
  right = len(arr)
  
  while left < right:
    mid = (left + right) // 2
    print("mid:::" + str(mid))
    if arr[mid] == key:
      return mid
    elif arr[mid] > key:
      right = mid
    else:
      left = mid + 1
  return None

tt_list = [1,2,5,6,8,9]
print("\n" + "=== 二分探索（出力） ===")
print(binary_search(tt_list))