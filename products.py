import os

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8')as f:
        for line in f:
            if '商品名稱,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
        
def user_input(products):
    while True:
        name = input("請輸入商品名稱:")
        if name == "q":
            break
        price = int(input("請輸入商品價格:"))
        products.append([name, price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):
    with open (filename, 'w', encoding = 'utf-8') as f:
        f.write('商品名稱,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + "\n")

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到檔案')
        products = read_file(filename)
    else:
        print('未找到檔案')

    products = read_file('products.csv')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()