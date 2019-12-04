import random
n = random.randint(1,100)
i = -1
while i<=0:
	num = int(input('請輸入一個1-100之間的整數'))
	if n == num :
		print('正確')
		i = 1
	elif n >num :
		print('比答案大')
	else:
		print('比答案小')