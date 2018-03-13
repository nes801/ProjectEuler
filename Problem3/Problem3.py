# 13195 の素因数は 5, 7, 13, 29 である.
#
# 600851475143 の素因数のうち最大のものを求めよ.

NUM=600851475143

#引数以上の素数を返す
def next_prime(tar_num):
    i=2
    while tar_num > i:
        if tar_num % i == 0 :
            tar_num+=1
            i=2
        else:
            i+=1
    return tar_num

i=2
while NUM > 1:
    if NUM % i == 0 :
        NUM=NUM/i
    else:
        i=next_prime(i+1)

print(i)
# 6857
