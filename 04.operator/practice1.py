'''
문제
파운드(lb)와 킬로그램(kg)을 상호 변환하는 프로그램 만들기

kg = pound * 0.453592
pound = kg * 2.204623
'''

data1 = int(input("파운드의 값을 입력하세요 : "))
data1_kilogram = data1 * 0.453592
print(f"파운드 {data1}의 킬로그램값은 {data1_kilogram:.2f} 입니다.")

data2 = int(input("킬로그램의 값을 입력하세요 : "))
data2_pound = data2 * 2.204623
print(f"킬로그램 {data2}의 파운드값은 {data2_pound:.2f} 입니다.")