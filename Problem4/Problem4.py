# 左右どちらから読んでも同じ値になる数を回文数という.
# 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
#
# では, 3桁の数の積で表される回文数の最大値を求めよ.

max=1
for i in range(999,99,-1):
    for j in range(999,99,-1):
        #積を文字列に変換
        num=str(i*j)
        #文字列を反転
        reverse=num[::-1]
        if(num==reverse):
            #最大値だったら更新
            max= i*j if i*j > max else max
            break
print(max)
#906609
