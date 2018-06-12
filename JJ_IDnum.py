
#coding=utf-8
__author__ = 'Felix'
import os
import random
from datetime import *
import time

# 随机生成身份证号

list_default = []

xing = ["赵","熊","吴","马","周","陈","许","何","陶","金","严","黄","毕","曹","仓","戴","狄","邓","龚","葛","韩","柯","令狐","司马","东方","上官","欧阳"]
ming = ["火舞","非","颜","振","晨","立","宇","明","俊","原","尘","泽","赫","独","玉","海","林","岩","琪拉","莫邪","露露","谷子","元芳","武藏","咬金","七号","尚香"]
codelist = ["421181","110101","120000","130800","130801","130802","130733","130730","130724","130722","130721","130706","130700"]
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射

def creat_Id():
    try:
        #global codelist
        #生成姓名
        name = xing[random.randint(0,len(xing))]+ming[random.randint(0,len(ming))]

        #身份证前6位
        id = codelist[random.randint(0,len(codelist))] #地区项

        #7-10位，出生年份
        year = str(random.randint(1950,2017))   #----年份项
        old = int(date.today().strftime("%Y"))-int(year)    #计算年龄
        id = id  #年份项

        #月份和日期项
        da = date.today()+timedelta(days=random.randint(1,366))
        birthday = year+da.strftime('%m%d')
        id = id + birthday

        #最后4位的随机前3位
        id = id + str(random.randint(100,300)) #顺序号简单处理

        #判断性别
        sex_index = id[16:]
        cus_sex = ""
        if int(sex_index)%2 ==0:
            cus_sex = "女"
        elif int(sex_index)%2 ==1:
            cus_sex = "男"

        #计算最后一位校验位
        sum_1 = 0
        for a in range(17):
            sum_1 = sum_1+int(id[a])*weight[a]
        index_id = sum_1%11
        result_id = id+str(checkcode[str(index_id)])    #最终身份证号码

        #处理用户信息数组
        list_default.insert(0,str(name))        #----姓名
        list_default.insert(1,cus_sex)          #----性别值
        list_default.insert(2,birthday)         #----生日值
        list_default.insert(3,str(old))         #----年龄值
        list_default.insert(4,result_id)        #----证件号码值

        return list_default
    except:
        #print(['阿凡达'])
        return ['阿凡达']
