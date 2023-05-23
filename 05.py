# ==========　リスト 問題 ============

[0,1,1,2,3,5,8,13,21,34,55,89,144]

fibo = [0,1,1,2,3,5,8,13,21,34,55,89]

######### 出力結果は同じだが、 リストの問題だから？ fibo.append(36 * 4) が正解
#fibo.append(36 * 4)
# fibo[-1] = 36 * 4

print(fibo)

# ========= リスト問題 02 ===============
x = ["a","b","c","d","e"]
print(x[:-3])

# ========= リスト　問題 03 ============
letters = ['a','b','c','d', 'e']
letters[-4:-2] = []
print(letters)

"""
解説
スライスの問題です。letter[-4:-2]=[] は次のように考えます。
例えば -1 の番地は最後の e を示します。これを踏まえると -4 はリストの b の位置です。 
: はそれ以降全てという意味です。
 -2 は d の位置です。この範囲を [] でリストを上書きするので、残るのは a, d, e になります。
 """

# ========= 文字スライス =========
arr_list = ["a", "b", "c", "d", "e", "f", "g"]

print (arr_list[0])
print (arr_list[1])
print (arr_list[2])
print (arr_list[3])
print (arr_list[4])
print (arr_list[5])
print (arr_list[6])

print (arr_list[-1])

print (arr_list[:-5]) # a, b
print (arr_list[-5:]) # c, d, e, f, g

print (arr_list[:3]) # a, b, c
print (arr_list[3:]) # d, e, f, g

import reprlib
reprlib.repr(set('diveintocode'))

#===============

import string

t = string.Template('My name is ${name}. I am ${age} years old.')
t.substitute({'name': 'Diop', 'age': 24})


#===============
def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4))
print(culc(4, 5))

print(3 ** 4)

from datetime import date
now = date.today()
print(now)

#=============================
pairs = [['Alice', 'Bob'],['Eve', 'Mike']]
pairs[1] = ['Don','Diop']

print(pairs)

#=============================

print(list(range(5)))

print(range(5))

#=============================
friends = ['Mary', 'Diop', 'Eve', 'Mike']

for i in enumerate(friends):

  print(i)

#=============================
total = 780

print('「お会計は', total , '円です。」')

#============================= 


menu = {'しまあじ': 400, 'たまご': 260, 'まぐろ': 500, 'サーモン':440}

def check(order):

  cnt = 0

  for i in order:
    cnt += menu[i]

  print(f'合計金額:{cnt}です')

o1 = {'まぐろ', 'しまあじ'}
check(o1)


#===========

diver = [d * 2 for d in 'diver']

for d in 'diver':
  print(d)

print(diver)

#===========
import json
x = {'name': 'yamada', 'data':[2,3,4]}
print(json.dumps(x))