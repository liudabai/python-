import json

with open("login.json",'r') as f:#读取文件取得用户名和密码
    login=json.load(f)
    username=login['username']
    password=login['password']
print("你正在登陆")
n=1
while n<4:
    enter_name=input('输入你的账户')
    if enter_name==username:
        n=1
        while True:
            enter_pass=input('输入你的密码')
            if enter_pass==password:
                print('登陆成功')
                exit()
            else:
                print("密码不对请重新输入")
                n=n+1
            if n>3:
                exit()
    else:
        n=n+1
        print('账户不对，请重新输入')


