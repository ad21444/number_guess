import random
start = int(input('隨機範圍起始值'))
end = int(input('隨機範圍結束值'))

n = random.randint(start,end)
a = 0
while True:
	print('請輸入一個在',start,'到',end,'之間的整數')
	num = int(input())
	if num>end or num<start:
		print('輸入錯誤')
	else:
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