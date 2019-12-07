'''
Одномерная динамика

Оловянный солдатик
Он ходит по шахматной доске.
В начале пути он стоит на линии 1 (не важно на какой вертикали, букве).
Каждый шаг он делает случайной ногой,
НО, одна нога ходит на 1 клетку, а другая на 2 клетки...
Пусть дана размерность доски, например - 4 клетки (доска 4х4)
Вопрос: сколько разных способов у солдатика на то, чтобы дойти до края стола?
'''


def get_1(n): # простая рекурсия
	if n <= 2:
		return 1
	else:
		return get_1(n - 1) + get_1(n - 2)


def get_2(n): # с меморизацией ...
	pass
	return 0


def get_3(n):  # динамикой ...
	pass
	return 0


import time

for n in range(29, 34):
	start = time.monotonic()
	result = get_1(n)
	finish = time.monotonic()
	dif = finish - start
	print('%3d%12d\t%10.3f' % (n, result, dif))