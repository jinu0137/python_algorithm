# [기초-종합] 16진수 구구단 출력하기
n = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%X" % (n, i, n*i))