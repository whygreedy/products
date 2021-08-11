import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			else:
				name, price = line.strip().split(',')
				products.append([name, price])
	return products


def print_product(products):
	print(products)


def user_input(products):
	while True:
		name = input('商品: ')
		if name == 'q':
			break
		price = input('價格: ')
		products.append([name, price])
	return products


def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	products = []
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('檔案存在')
		products = read_file(filename)
		print_product(products)
	else:
		print('檔案不存在')
	products = user_input(products)
	write_file(filename, products)


main()