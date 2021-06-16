import re
import os



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

def fianl_reference():
    dizhi = input("Input the copy wenxian:")
    dizhi_new = re.split('．', dizhi) #看情况更改，一般都是句号  复制最好，不要手打!!!
    name = dizhi_new[0]  # Chaoqun,Wu Yue,Tian Xinmei,Huang Jianqiang,Hua Xian-Sheng
    name_list = list(name.split(","))  # ['Wan Chaoqun', 'Wu Yue', 'Tian Xinmei', 'Huang Jianqiang', 'Hua Xian-Sheng']
    part1 = get_name(name, len(name_list))#part1 表示作者们 ,加了空格
    part2 = dizhi_new[1] + ", "           #part2 表示论文题目 ,加了空格
    other_part = dizhi_new[2]
    other_part_split = other_part.split(',')

    part3 = other_part_split[0] + ', '  # part3 表示哪个期刊  ,加了空格

    part4 = other_part_split[1] + ', '  # part4 表示哪一年出版 ,加了空格

    vol_num_page = other_part_split[2]

    vol_num_page_split = vol_num_page.split(':')

    part5 = vol_num_page_split[0] + ": " # part5 表示 期卷 ,加了空格
    part6 = vol_num_page_split[1] + '.'  # part6 表示页码 ,加了空格

    fianl_reference = part1 + part2 + part3 + part4 + part5 + part6
    return fianl_reference


if __name__ == "__main__":
    out = fianl_reference()
    print(out)



# dizhi = input("Input the copy wenxian:")
# dizhi_new = re.split('．',dizhi)#["xcv xvsd fgsdg“,"fsdw eefwfs fs","wet gwg sd gaga"]
#
# #print(dizhi_new[0],'\n',dizhi_new[1],'\n',dizhi_new[2])
# name = dizhi_new[0]#Chaoqun,Wu Yue,Tian Xinmei,Huang Jianqiang,Hua Xian-Sheng
# name_list = list(name.split(","))#['Wan Chaoqun', 'Wu Yue', 'Tian Xinmei', 'Huang Jianqiang', 'Hua Xian-Sheng']
# part1 = get_name(name,len(name_list))
# print("name###",part1)                #part1 表示作者们
#
# part2 = dizhi_new[1]+". "              #part2 表示论文题目
# print("paper_name###",part2)
#
# other_part = dizhi_new[2]
# other_part_split = other_part.split(',')
#
# part3 = other_part_split[0]+', '      #part3 表示哪个期刊
#
# part4 = other_part_split[1]+', '      #part4 表示哪一年出版
#
# vol_num_page = other_part_split[2]
#
# vol_num_page_split = vol_num_page.split(':')
#
# part5 = vol_num_page_split[0]+": "   #part5 表示 期卷
# part6 = vol_num_page_split[1]+'.'    #part6 表示页码
#
# fianl_reference = part1+part2+ part3 +part4+part5+part6
# print("final",fianl_reference)
#
#
# # if __name__ == "__main__":