password = str('a123456')

x = 3
while x > 0:
	x = x - 1
	pw = input('請輸入密碼: (最多有3次機會)')
	if pw != password:
		if x == 0:
			print('密碼錯誤!, 你沒機會了')
			break	
		print('密碼錯誤! 還有', x, '次機會')	
	else:
		print('登入成功!')
		break
	