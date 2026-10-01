# 변수 : 어떤 자료형이든 상관없이 넣을 수 있다. 
var1 = 'Hello Python'
print(var1)
print(id(var1)) # 객체가 들어가 있는 주소

var1 = 100 # 객체를 새로생성하고 변수의 주소를 바꿔주는것이다. 
print(var1)
print(id(var1))

# 아무리 큰 데이터라도 다 넣을수있음 -> 빅데이터 분석에 사용

# 변수명 지정
# 변수가 무엇을 가리키는지 알 수 있는 이름으로 작명 

age = 23
name = '이명수'

# 예약어
# import 로 변수를 지을 수 없음

# 10.01 수업

# python의 자료의 크기는 상관없다. 
num1 = 100
num2 = 438463843843846384384387398359851348
num3 = 9.56564943813834

c = '홍길동 아무개'
s = 'Hello world!!!'
b =  True

print(num1)
print(num2)
print(num3)
print(c)
print(s)
print(b)

print("-"*30)

print('num1 type =', type(num1))
print(f'num2 type = {type(num2)}')
print(f'num3 type =  {type(num3)}')
print(f'c type = {type(c)}')
print(f's type =  {type(s)}')
print(f'b type =  {type(b)}')

print("-"*30)

a = 1
b = 2
c = 3
d, e, f = 1, 2, 3 # 변수선언 한꺼번에도 가능함

print(d, e, f)

g, h, i = '더조은', False, 3.5984

print(g, h, i)