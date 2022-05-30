import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字結束值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
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


		
