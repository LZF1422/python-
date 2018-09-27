# TODO: 作为一个用户，我应该有如下的体验：
    #    # 查看剩余的票数，这样我才能知道现在买票的重要性
    #    # 程序应该以我的名字欢迎我，这样我才觉得这个买票网站比较人性化
        # 如果票数充足，我应该可以购买我想要的数量，并且程序会提示我总票价
        # 如果票数不足或售罄，程序应该告知我无法继续买票
        # 在购票前，程序应该让我确认订单，这样我才不会不小心购买不想要的票
        # 如果我误操作，程序应该让我看到简单明了的错误提示

        # 票价自定
        # 剩余票数自定
        # 你可能会用到这个清屏函数：
    #    import os  # 首先需要导入 os 模组

    #    def clear_screen():  # 这个函数一旦被调用会对控制台进行清屏
    #        os.system('cls')

import re
import random
#票数随机生成
#重庆到贵阳的票数
cq_gy = random.randint(0,40)
#这是单价
cq_gy_dj = 40
#重庆到北京
cq_bj = random.randint(0,40)
cq_bj_dj = 35
#重庆到上海
cq_sh = random.randint(0,40)
cq_sh_dj = 34

output = []
outp = []

def gpps():
    while True:
        try:
            yy_sl = int(input("您需要购买的票的数量："))
            if(yy_sl == 0):
                print("票数不能为0！")
                continue
            return yy_sl
        except ValueError:
            print("票数只能为数字，请正确输入")

#用户购票的输入信息
def gpxx():
    while True:
        #用户输入错误，用循环实现重新输入
        #限制购买的班次和票数只能为数字
        while True:
            try:
                yy = int(input("您需要购买的票为(输入对应班次的序号)："))
                break
            except ValueError:
                print("票只能为数字，请正确输入")

     #班次为 1 (重庆到贵阳的) ，调用购票函数，并传入对应的参数
        if(yy == 1):
            yy_sl = gpps()
            m = gp(cq_gy,cq_gy_dj,yy,yy_sl,"重庆到贵阳")
            #这个是购票函数里有最外层循环的break，会报错，用参数传出来，再break
            #1 or 2
            lp = m.pop()
            #票数
            ll = m.pop()
            if(lp == 1):
                outp.append(ll)
                outp.append(1)
                return outp
            else:
                continue
        #班次为 2 (重庆到北京的) ，调用购票函数，并传入对应的参数
        elif(yy == 2):
            yy_sl = gpps()
            m = gp(cq_bj,cq_bj_dj,yy,yy_sl,"重庆到北京")
            lp = m.pop()
            #票数
            ll = m.pop()
            if(lp == 1):
                outp.append(ll)
                outp.append(2)
                return outp
            else:
                continue
        #班次为 3 (重庆到上海的) ，调用购票函数，并传入对应的参数
        elif(yy == 3):
            yy_sl = gpps()
            m = gp(cq_sh,cq_sh_dj,yy,yy_sl,"重庆到上海")
            lp = m.pop()
            #票数
            ll = m.pop()
            if(lp == 1):
                outp.append(ll)
                outp.append(3)
                return outp
            else:
                continue
        else:
            print("班次未上线！")
            gpxx()


#购票函数
def gp(cq_gy,cq_dj,yy,yy_sl,df):
    #判断购买的票数是否小于现有票数  和   购买的票数要大于0
    if(yy_sl <= cq_gy and yy_sl > 0):
        print("您购买的是从重庆到{}的列车票，票数{}张，总价{}元。".format(df,yy_sl,yy_sl * cq_dj))
        qr = input("是否确认购买？(Y/N)\n")
        #判断Y/N的输入
        while True:
            if(qr == "Y".lower() or qr =="Y".upper):
                cq_gy -= yy_sl
                print("购票成功")
                break
            elif(qr == "N".lower() or qr =="N".upper):
                print("返回购票页面.")
                break
            else:
                qr = input("请正确输入Y/N\n")
        if(qr == "Y".lower() or qr =="Y".upper):
            output.append(cq_gy)
            output.append(1)
            return output
        elif(qr == "N".lower() or qr =="N".upper):
            output.append(cq_gy)
            output.append(2)
            return output
    elif(yy_sl > cq_gy):
        print("{}的票数不足!".format(df))
        output.append(cq_gy)
        output.append(2)
        return output
    else:
        print("票数只能为正整数！")

#购票信息
yh = input("用户名:")
print("欢迎您进入购票系统，{}".format(yh))
print("——————————————————————————————————————————————————————————")
print("\n\t\t\t\t\t\t买票系统\t\t\t\t\n")
print("\t1.重庆到贵阳\t票数：{}\t单价：{}\t".format(cq_gy,cq_gy_dj),end = '')
print("2.重庆到北京\t票数：{}\t单价：{}\n".format(cq_bj,cq_bj_dj))
print("\t3.重庆到上海\t票数：{}\t单价：{}\n".format(cq_sh,cq_sh_dj))
p = gpxx()
ii = p.pop()
oo = p.pop()
df = ""
jq = 0
if(ii == 1):
    df = "重庆到贵阳"
    ps = (cq_gy - oo)
    jq = ps * cq_gy_dj
    cq_gy = oo
elif(ii == 2):
    df = "重庆到北京"
    ps = (cq_bj - oo)
    jq = ps * cq_bj_dj
    cq_bj = oo
else:
    df = "重庆到上海"
    ps = (cq_sh - oo)
    jq = ps * cq_sh_dj
    cq_sh = oo

print("——————————————————————————————————————————————————————————")
print("\n\t\t\t\t\t\t买票系统\t\t\t\t\n")
print("\t1.重庆到贵阳\t票数：{}\t单价：{}\t".format(cq_gy,cq_gy_dj),end = '')
print("2.重庆到北京\t票数：{}\t单价：{}\n".format(cq_bj,cq_bj_dj))
print("\t3.重庆到上海\t票数：{}\t单价：{}\n".format(cq_sh,cq_sh_dj))
print("\t您的票是从{},票数为{}张,总花费{}元.".format(df,ps,jq))
print("——————————————————————————————————————————————————————————")
llll = input("按回车键结束")
