# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import time
import copy
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_idNum_main import Ui_MainWindow
from JJ_IDnum import creat_Id,checkcode,weight
from datetime import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #设置列宽
        self.tableWidget.setColumnWidth(0,40)   #序号
        self.tableWidget.setColumnWidth(1,90)   #姓名
        self.tableWidget.setColumnWidth(2,49)   #性别
        self.tableWidget.setColumnWidth(3,80)   #出生年月日
        self.tableWidget.setColumnWidth(4,55)   #年龄
        self.tableWidget.setColumnWidth(5,180)  #证件号码

        #设置出生日期列表宽度
        self.tableWidget_birthInfo.setRowHeight(0,30)
        self.tableWidget_birthInfo.setColumnWidth(0,65)   #年
        self.tableWidget_birthInfo.setColumnWidth(1,35)
        self.tableWidget_birthInfo.setColumnWidth(2,65)   #月
        self.tableWidget_birthInfo.setColumnWidth(3,35)
        self.tableWidget_birthInfo.setColumnWidth(4,65)   #日
        self.tableWidget_birthInfo.setColumnWidth(5,35)

    @pyqtSlot()
    def on_pushButton_clicked(self):

        """
        Slot documentation goes here.
        """
        try:
            #随机生成客户5要素信息：
            id_list = []    #客户5要素信息列表
            i_3=0
            while i_3 < 6 :
                creat_Id().clear()
                cust_info = creat_Id()
                temp_id = copy.deepcopy(cust_info)
                if temp_id == ['阿凡达']:
                    pass
                else:
                    id_list.append(temp_id)
                    i_3 = i_3 + 1

            #填写身份证号码到对应的单元格中
            for i_2 in range(5):
                for cus_id1 in range(5):
                    a1 = self.tableWidget.item(int(i_2)+1,cus_id1+1)
                    a1.setText(id_list[i_2][cus_id1])
            id_list.clear()
        except:
            pass

    @pyqtSlot(bool)
    def on_radioButton_Boy_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if self.radioButton_Girl.isChecked():
            self.radioButton_Girl.released()
    
    @pyqtSlot(bool)
    def on_radioButton_Girl_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        if  self.radioButton_Boy.isChecked():
            self.radioButton_Boy.released()

    @pyqtSlot()
    def on_pushButton_GJSC_clicked(self):
        """
        Slot documentation goes here.
        """
        _translate = QtCore.QCoreApplication.translate
        import random
        from JJ_IDnum import codelist

        now_id = ""
        while(now_id == ""):
            try:
                id_Full = codelist[random.randint(0,len(codelist))]                 #地区项

                #生日项
                birth_Year = str(self.tableWidget_birthInfo.item(0,0).text())
                birth_month = str(self.tableWidget_birthInfo.item(0,2).text())
                birth_day = str(self.tableWidget_birthInfo.item(0,4).text())

                if birth_Year == "":
                    birth_Year = str(random.randint(1950,2017))
                if birth_month == "":
                    birth_month = str(random.randint(1,12)).zfill(2)
                else:
                    birth_month=birth_month.zfill(2)
                if birth_day == "":
                    birth_day = str(random.randint(1,28)).zfill(2)
                else:
                    birth_day=birth_day.zfill(2)

                id_Full_1 = id_Full+birth_Year+birth_month+birth_day              #地区项+生日项

                #最后四位
                #----1-2
                last_two = str(random.randint(0,99)).zfill(2)
                id_Full_2 = id_Full_1 + last_two                                    #最后四位的前2位
                #----3
                boy_sign = ["1","3","5","7","9"]
                girl_sign = ["0","2","4","6","8"]
                all_sign = boy_sign+girl_sign
                if self.radioButton_Boy.isChecked():
                    sex_sign = boy_sign[random.randint(0,len(boy_sign))]
                elif self.radioButton_Girl.isChecked():
                    sex_sign = girl_sign[random.randint(0,len(girl_sign))]
                else:
                    sex_sign =all_sign[random.randint(0,len(all_sign))]
                id_Full_3 = id_Full_2 +sex_sign                                     #添加性别位
                #最后一位
                sum_1 = 0
                for a_23 in range(17):
                    sum_1 = sum_1+int(id_Full_3[a_23])*weight[a_23]
                index_id = sum_1%11
                id_Full_final = id_Full_3+str(checkcode[str(index_id)])    #最终身份证号码

                self.textBrowser_IDShow.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#ff5500;\">"+id_Full_final+"</span></p></body></html>"))

                #显示年龄和性别信息
                old_1 = int(date.today().strftime("%Y"))-int(birth_Year)
                sex_1 = "--"
                if int(sex_sign)%2 ==0:
                    sex_1 = "女"
                elif int(sex_sign)%2 ==1:
                    sex_1 = "男"
                beizhu_old = "年龄： "+str(old_1)+"岁"
                beizhu_sex = "性别： "+str(sex_1)
                self.label_Age.setText(beizhu_old)
                self.label_Sex.setText(beizhu_sex)

                now_id = "1"

            except:
                now_id = ""
                #print("Error !!")
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
