import random
n = random.randint(1,100)
i = -1
a = 0
while True:
	num = int(input('請輸入一個1-100之間的整數'))
	a = a +1
	if n == num :
		print('答案正確')
		print('共猜了', a ,'次')
		break
	elif n >num :
		print('猜的數字比答案小')
	else:
		print('猜的數字比答案大')
	print('已經猜了', a ,'次')