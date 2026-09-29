print(1,3,5)
print('아무개씨','안녕하세요')
print("-"*20)
# 구분자 + 는 문자열 일때는 연결하여 출력(띄어쓰기 안함)
print(1+3+5)
print('홍길동'+'아무개')

# + 기호는 반드시 타입이 맞아야 한다.
# print(1 + '홍길동') # 에러 -> 자료형이 같아야 한다. 
print(str(1) + '홍길동') # 자료형 변환하면 사용 가능

print(1, '홍길동') # ctrl / 주석처리 단축키
print("-"*20)
# 서식 출력 %d decimal 정수, %f float 실수, %s string 문자열

print("정수 : %d, 실수 : %f, 문자열 : %s " %(5, 3.14, '홍길동')) # 자리지정할때 이런 형식을 많이 사용함. 

# 자리지정 %자리수d(정수), %자리수<소수점도 포함. 소수점 이하의 자리개수>f(실수), %자리수s(문자열)
print("정수 : %3d, 실수 : %6.4f, 문자열 : %5s " %(5, 3.14, '홍길동'))

print('실수 소수점 둘째 자리까지만 출력 : %.2f,%.2f,%.2f' %(12.1546, 18226, 2.71826))
print("-"*20)

# sep 속성
# : 분리 문자 설정 - 기본적으로 분리문자 공백하나가 들어가 있다
print(5,7.7,'더조은',True, sep = ' ') # sep 안넣으면 기본값 sep = ' '
print(5, 7.7, '더조은', True, sep = '/')
print(5, 7.7, '더조은', True, sep = ' / ')
print(5, 7.7, '더조은', True, sep = ',')
print('-'*30)

print('오늘은\n수요일\n공부하는 날')
print('')
# end 속성 : 마지막문자 설정
print('hello', end = '\n')
print('python', end = '')
print('더조은', end = '\n')
print('python', end='\t')
print('강남')

print("-"*20)

print("{}, {}, {}".format(100,'Hello', 3.14159))
print('{1}, {2}, {0}'.format(100, 'Hello', 3.14159))
print('이름 : {}, 나이 : {}, data = {}'.format('홍길동', 21, 3826.545))
print('이름 : {1}, 나이 : {2}, data = {0}'.format(3826.545, '홍길동', 21 ))

print(format(3.14159))
print(format(3.14159, '.2f'))
print('원주율 =', format(3.14159))
print('원주율 = {}'.format(3.14159))
print('원주율 = ',format(3.14159, '.2f'))
print('원주율 = {}{}'.format(3.14159, '.2f'))
print('금액 : ', format(10000, '7d'))
print('금액 : ', format(5000, '7d'))
print('금액 : ', format(486468464000, '3,d')) # 3자리마다 , 넣기, 컴마는 보여줄때만 그렇지 실제 형식은 정수임. 

