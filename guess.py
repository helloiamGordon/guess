import random
r = random.randint(1, 10)
count = 0
while True :
	count = count + 1
	num = input("請猜數字: ")
	num = int(num)
	if num == r :
		print('恭喜答對了!!')
		print('您猜',count,'次')	
		break
	else :
		if num > r :
			print('比答案大')
		else :
			print('比答案小')
	print('您猜',count,'次')		


		
