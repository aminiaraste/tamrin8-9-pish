
PRODUCTS =[]
def read_load_from_file():
    print("Loading...")
    f = open('database.csv' , 'r')

    for row in f :
        info = row[:-1].split(',')
        new_dict = {'code': info[0], 'name': info[1],'price': info[2], 'count': info[3]}
        PRODUCTS.append(new_dict)
    print(PRODUCTS)
    print('database loaded . app is ready to use')




def add():
    code = int(input('enter number of code :'))
    name = input('enter name:')
    price = int(input('enter price :'))
    count = int(input('enter number: '))
    new_dict = {'code': code, 'name': name ,'price': price , 'count': count}
    PRODUCTS.append(new_dict)
            
    print(PRODUCTS)
def buy():
    basket = []
    print('1-afzodan be sabad kharid')
    print('2-exite and print ')
    choice = int(input('ghasd shoma chist?'))
    while True:
        if choice ==1:
            name = input('enter the name of item :')
            count = int(input('how much ?'))
            for product in PRODUCTS:
                if product['name'] == name:
                    if count <= int(product['count']):
                        temp = int(product['count'])
                        product['count'] = count
                        basket.append(product)
                        print(basket)
                        product['count'] = temp - count
                        PRODUCTS.append(product['count'])
                        break
            break
        else:
            print('exit')
            break
def search():
    name = input("enter your name : ")
    for product in PRODUCTS:
        if product['name'] == name:
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'],'\t')
def edit():
    show_list()
    name = input("enter your name : ")
    for product in PRODUCTS:
        if product['name'] == name:
            choice =int(input('which one do you want to change ?: 1- code / 2- count / 3-price /4- name '))
            if choice == 1:
                product['code'] = int(input(' enter  new code :'))
            elif choice == 2:
                product['count'] = int(input('enter new count :'))
            elif choice == 3:
                product['price'] = int(input('enter new price :'))
            elif choice == 4 :
                product['name'] = input('change this name :')
            PRODUCTS.append(product)
            print(product)
    else:
        print('not found')
            
def show_list():
    print('code\tname\tprice\tcount')
    for product in PRODUCTS:
        print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'],'\t')
def delet():
    show_list()
    name = input("enter your name : ")
    for product in PRODUCTS:
        if product['name'] == name:
            PRODUCTS.remove(product)
            print(PRODUCTS)
def show_menu():
    print("welcome to sajjad store")
    print("1-Add")
    print(("2-Edit"))
    print("3-Delete")
    print("4- show list")
    print("5-search")
    print("6-buy")
    print("save and exit")


read_load_from_file()
while True:
    show_menu()
    choice = int(input("enter your choice : "))
    if choice == 1 :
        add()
    elif choice == 2 :
        edit()
    elif choice == 3 :
        delet()
    elif choice == 4 :
        show_list()
    elif choice == 5 :
        search()
    elif choice == 6 :
        buy()
    




