import re
def get_name(dizhi,n):
##############################################################
# 功能：得到参考文献的名字，并且按照名字第一个字母. 空格姓氏，
#eg  ；   Li Zhaoyang  得到  Z. Li
#n 为复制的参考文献有k个人则n=k;dizhi为网上复制的参考文献
# 必须 姓名在前，名字在后   引用格式：GB/T 7714-2015
#https://www.zhangqiaokeyan.com/ 按照这个网址给的格式编程
##############################################################
    dizhi_new = dizhi.split(",", n)
    name_list = []
    for i in range(n):
        name1 = dizhi_new[i]  # Wan Chaoqun

        name1_split = re.split(r"[ ]+", name1)  # ['Wan', 'Chaoqun']
        name1_xing = name1_split[0]
        name1_zimu = list(name1_split[1])[0]
        name1_final = ". ".join((name1_zimu, name1_xing))
        if i==n-1:
            name1_final = name1_final+'. '
        name_list.append(name1_final)
    final_name = ", ".join(name_list)
    return final_name

if __name__ == "__main__":
    dizhi = input("dizhi:")
    n = int(input('n:'))
    final = get_name(dizhi,n)
    print(final)