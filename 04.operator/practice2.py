coffee1 = 500
coffee2 = 1800
kimbob1 = 900
kimbob2 = 1400
milk1 = 800
milk2 = 1800
do1 = 3500
do2 = 4000
coke1 = 700
coke2 = 1500
shrimp1 = 1000
shrimp2 = 2000

# 잔액
budget = 100000

buy1 = 0
buy2 = 0 
get1 = 0
get2 = 0
get3 = 0
get4 = 0
get5 = 0

buy1 += buy1 + kimbob1*-10
buy2 += buy2 + do1*-5
get1 += get1 + milk2*2
get2 += get2 + do2*4
get3 += get3 + coke2*1
get4 += get4 + shrimp2*4
get5 += get5 + coffee2*5

final = buy1 + buy2 + get1 + get2 + get3 + get4 + get5

total = budget - final
print(total)
