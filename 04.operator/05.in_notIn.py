"""
소속연산자

in : 어떤 데이터가 특정 데이터 안에 있는지 검사
     -> True : 있다
     -> False : 없다

not in : 어떤 데이터가 특정 데이터안에 없는지 검사
     -> True : 없다
     -> False : 있다


"""

str = 'abcdefg'
print('ab' in str)
print('xy' in str)
print('dg' in str)
print("-"*20)

print('ab' not in str)
print('xy' not in str)
print('dg' not in str)