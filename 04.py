### numpy インポート
import numpy as np

a = np.array([1,2,3])
print(a)

### オブジェクトの型を確認
print(type(a))

### NumPyのshapeメソッドを使ってデータ構造を確認
# 出力結果  (3,)  ３つの要素をもつ 1次元配列
kata = a.shape
print(kata)

### 明示的に次元数を知りたい場合 ndim
zigen = a.ndim
print(zigen)

###### ２次元配列 ######
b = np.array([[1,2,3], [4,5,6]])
print(b)

b_arr = b.shape
### 出力結果：(2, 3) 上記の結果は、2行３列からなる2次元配列であることを意味する。
print(b_arr)

#################### スライス ###################
### スライスでの ２次元配列の出力
# b = np.array([[1,2,3], [4,5,6]]) => 出力結果 3, 6
print(b[:, 2])

b[:, 2] = 8
print(b)

b[1, :] = 8
print(b)



#==== format の書式
print ('こんにちは！{}さん'.format('山田'), end="\n\n")

#==== 書式指定に ;, を用いると、数値をカンマ区切りで表示できます。
print('{:,f}'.format(100000000))

#==== format の配列
price = [200, 300, 500]

print('ハンバーガー:{0[1]}円 ポテト:{0[0]}円 セット: {0[2]}'.format(price) , end="\n\n")


#============ python インタプリタ問題

arr_list = [6,[5,[1,2]],4,[3,0]]

print(arr_list[0])
print(arr_list[1])
print(arr_list[2])
print(arr_list[3], end="\n\n")

#=================== list zip の問題

dic = [
    ['Noro', 'Nakao', 'Miyaoka'],
    ['Kimura', 'Miyashita', 'Shibata'],
    ['Matsumoto', 'Tanaka', 'Ivan']
]

# print(list(zip(*dic)))

