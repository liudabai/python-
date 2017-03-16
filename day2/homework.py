all_list=[11,22,33,44,55,66,77,88,99,90,]


def main(all_list):
    """
    dic={'k1':[],'k2':[]}
    for n in range(len(num)):
        del_num=num.pop()
        if del_num>66:
            big_num=dic['k1']
            big_num.append(del_num)
            dic['k1']=big_num
        else:
            small_num=dic['k2']
            small_num.append(del_num)
            dic['k2']=small_num
    print(dic)
"""
    dic={}
    for i in all_list:
        if i >66:
            if "k1" in dic.keys():
                dic['k1'].append(i)
            else:
                dic['k1']=[i,]
        elif i<=66:
            if "k2" in dic.keys():
                dic['k2'].append(i)
            else:
                dic['k2']=[i,]   # 因为我们想要 dic={"k1":[11,22,33,44]}

    print(dic)
if __name__=='__main__':
    main(all_list)