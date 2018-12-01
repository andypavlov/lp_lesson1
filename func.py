def get_summ(one, two, delimiter=' '):
	if (type(one) == int or type(one) ==float) and (type(two) == int or type(two) == float):
		print('Это числа')
		return one + two
	elif (type(one) is list or type(one) is tuple) and (type(two) is list or type(two) is tuple):
		print('Это списки')
		return one + two
	else:
		print('Это строки')
		return '{0}{1}{2}'.format(one.upper(), delimiter, two.upper())

sum_string = get_summ(3, 2)
print(sum_string)

sum_string = get_summ(4.5, 5.7)
print(sum_string)

sum_string = get_summ([1, 2, 3], [4, 5, 6])
print(sum_string)

sum_string = get_summ ('Learn', 'python')
print(sum_string)
