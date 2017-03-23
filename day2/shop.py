

def show_good():  #展示商品和价格
    global shop_goods
    shop_goods={'basketball': 110, 'T-shirt': 50, 'shoe': 200, 'chair': 800, 'bowl': 5, }
    global shop_goods_names
    shop_goods_names=list(shop_goods.keys())
    for k,v in enumerate(shop_goods_names):
        print(k,' : ',v,':',shop_goods[v],'$')

def cart():  #加入购物车
    shop_cart=[]
    while True:
        good=input("输入你想买的物品的编号,退出请输入q")
        if good=='q':
            break
        good=int(good)
        shop_cart.append(shop_goods_names[good])
    return shop_cart

def calculate_expense(shop_cart): #计算金额
    expense = 0
    for good in shop_cart:
        expense+=shop_goods[good]
    print('总花费%s'%expense)
    return expense

def judge(money,shop_cart): #判断是否买多了
    expense=calculate_expense(shop_cart)
    while expense>money:
        print('你的余额为%s,余额不足'% money)
        for k, v in enumerate(shop_cart):
            print(k,':',v,':',shop_goods[v],'$')
        abandon_good=input('请去除一些商品')
        expense -= shop_goods[shop_cart[int(abandon_good)]]
        shop_cart.remove(shop_cart[int(abandon_good)])
        expense = calculate_expense(shop_cart)
    return shop_cart

def main(money):
    show_good()
    shop_cart=cart()
    shop_cart=judge(money,shop_cart)
    expense=calculate_expense(shop_cart)
    money=money-expense
    print('还剩%s'%money)

if __name__=="__main__":
    money=1000
    main(money)