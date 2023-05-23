import numpy as np # NumPy をインポート
import matplotlib.pyplot as plt # Matplotlib が持つ "pyplot" をインポート

fig = plt.figure() # 画像の表示領域を設定

# 最初の 10個のデータについて同じ処理を繰り返す
for i, x in enumerate(X[0:10] , 0):
  sp = fig.add_subplot(2, 5, (i + 1)) ## 各数字を表示するための区画を設定
  sp.imshow(x.reshape(8, 8), cmp = "gray") ## 数字画像の表示