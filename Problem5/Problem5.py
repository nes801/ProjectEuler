# 2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり,
# そのような数字の中では最小の値である.
#
# では, 1 から 20 までの整数全てで割り切れる数字の中で
# 最小の正の数はいくらになるか.


#引数以上の素数を返す関数
def next_prime(tar_num):
    i=2
    while tar_num > i:
        if tar_num % i == 0 :
            tar_num+=1
            i=2
        else:
            i+=1
    return tar_num


#各値(1～20)を素因数分解する
#それぞれの素数の一番大きかった指数を採用
##1～20の配列を0初期化で用意しておいて、指数を入れておく
##入ってなかったら指数なしってことで
#最後に配列の中身を全部かけて足し合わせる


NUM =20

#NUM個分の指数を入れるリストを0で初期化
list=[0 for i in range(NUM+1)]

#各値(1～20)をひとつずつ素因数分解する
for n in range(1,NUM+1):
    i=2
    #リストのコピー作成
    copy_list=[0 for i in range(NUM+1)]
    while n > 1:
        if n % i == 0 :
            n=n/i
            #指数を+1
            copy_list[i]+=1
        else:
            i=next_prime(i+1)
    #本番用のリストより大きい指数があれば更新
    for i in range(len(list)):
        if list[i]<copy_list[i]:
            list[i]=copy_list[i]

print(list)
SUM=1
for i in range(len(list)):
    #指数が0だったら飛ばす
    if list[i] !=0:
        #全部の指数を掛け合わせる
        SUM *= i**list[i]

print(SUM)

#232792560
