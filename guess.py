import random
r = random.randint(1, 10)
while True :
	num = input("請猜數字: ")
	num = int(num)
	if num == r :
		print('恭喜答對了!!')
		break
	else :
		if num > r :
			print('比答案大')
		else :
			print('比答案小')


		
