# 17배
n = int(input(), 2)     # n을 2진수로 입력받음
n *= 17                 # n에 17을 곱함
print(bin(n)[2:])       # bin() : 10진수를 2진수 문자열로 변환(ex: 0b1000) 후 앞의 0b를 제거