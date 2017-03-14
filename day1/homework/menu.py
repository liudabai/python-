import json
with open('menu.json','r') as f:
    menu=json.load(f)

one_menu=list(menu.keys())
for index,item in enumerate(one_menu,start=1):
    print(index,item)
enter_one=input('>>')
enter_one_menu=one_menu[int(enter_one)-1]
two_menu=list(menu[enter_one_menu].keys())
for index,item in enumerate(two_menu,start=1):
    print(index,item)
enter_two=input('>>')
enter_two_menu=two_menu[int(enter_two)-1]
three_menu=menu[enter_one_menu][enter_two_menu]
for index,value in enumerate(three_menu,start=1):
    print(index,value)
enter_three_menu=input(">>")
selected_menu=three_menu[int(enter_three_menu)-1]
print(selected_menu)