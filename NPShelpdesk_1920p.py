# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.font import *
from datetime import datetime

win = Tk()
win.title =("NPS - Client Guidance System")
win.geometry("1920x1080")
win.option_add("*Font", "Arial 32")

#=======================Scene3=======================
def ilban():
    txt_Scene3_annae_1_label.destroy()
    txt_Scene3_annae_2_label.destroy()
    txt_Scene3_annae_3_label.destroy()
    txt_Scene3_annae_4_label.destroy()
    button_Scene3_ilban.destroy()
    button_Scene3_saupjang.destroy()
    button_Scene3_jiyeok.destroy()

    txt_Scene3_1_annae_1 = "일반상담 창구는 앞쪽의 1~4번 창구입니다."
    txt_Scene3_1_annae_2 = "번호표를 뽑고 잠깐 기다려주십시오. 이용해주셔서 감사합니다."
    txt_Scene3_1_annae_1_label = Label(text = txt_Scene3_1_annae_1)
    txt_Scene3_1_annae_2_label = Label(text = txt_Scene3_1_annae_2)
    txt_Scene3_1_annae_1_label.place(x = 500+150, y = 360-100)
    txt_Scene3_1_annae_2_label.place(x = 390+150, y = 500-100)
    button_ilban_cheoum = Button(text = "처음으로")
    button_ilban_cheoum.place(x = 820, y = 600, width = 200, height = 300)
    button_ilban_cheoum.config(command = win.destroy)

def saupjang():
    txt_Scene3_annae_1_label.destroy()
    txt_Scene3_annae_2_label.destroy()
    txt_Scene3_annae_3_label.destroy()
    txt_Scene3_annae_4_label.destroy()
    button_Scene3_ilban.destroy()
    button_Scene3_saupjang.destroy()
    button_Scene3_jiyeok.destroy()

    txt_Scene4_1_annae_1 = "사업장 담당 창구는 가장 안쪽에 있습니다."
    txt_Scene4_1_annae_2 = "이용해주셔서 감사합니다."
    txt_Scene4_1_annae_1_label = Label(text = txt_Scene4_1_annae_1)
    txt_Scene4_1_annae_2_label = Label(text = txt_Scene4_1_annae_2)
    txt_Scene4_1_annae_1_label.place(x = 520+150, y = 360-100)
    txt_Scene4_1_annae_2_label.place(x = 600+150, y = 500-100)

    button_saupjang_cheoum = Button(text = "처음으로")
    button_saupjang_cheoum.place(x = 820, y = 600, width = 200, height = 300)
    button_saupjang_cheoum.config(command = win.destroy)

def jiyeok():
    txt_Scene3_annae_1_label.destroy()
    txt_Scene3_annae_2_label.destroy()
    txt_Scene3_annae_3_label.destroy()
    txt_Scene3_annae_4_label.destroy()
    button_Scene3_ilban.destroy()
    button_Scene3_saupjang.destroy()
    button_Scene3_jiyeok.destroy()

    txt_Scene4_annae_1 = "맨 안쪽으로 가신 후, 오른쪽으로 가시면 됩니다."
    txt_Scene4_annae_2 = "이용해주셔서 감사합니다."
    txt_Scene4_annae_1_label = Label(text = txt_Scene4_annae_1)
    txt_Scene4_annae_2_label = Label(text = txt_Scene4_annae_2)
    txt_Scene4_annae_1_label.place(x = 480+150, y = 360-100)
    txt_Scene4_annae_2_label.place(x = 600+150, y = 500-100)

    button_jiyeok_cheoum = Button(text = "처음으로")
    button_jiyeok_cheoum.place(x = 820, y = 600, width = 200, height = 300)
    button_jiyeok_cheoum.config(command = win.destroy)

def go_to_Scene3():
    txt_Scene2_annae_1_label.destroy()
    txt_Scene2_annae_2_label.destroy()
    txt_Scene2_annae_3_label.destroy()
    txt_Scene2_annae_4_label.destroy()
    button_Scene2_yeonjiboo.destroy()
    button_Scene2_daum.destroy()

    global txt_Scene3_annae_1_label, txt_Scene3_annae_2_label, txt_Scene3_annae_3_label, txt_Scene3_annae_4_label, button_Scene3_ilban, button_Scene3_saupjang, button_Scene3_jiyeok
    txt_Scene3_annae_1 = "서류를 발급받으시려는 경우, 일반 상담을 원하시는 경우"
    txt_Scene3_annae_2 = "일반상담 버튼을 눌러주세요."
    txt_Scene3_annae_3 = "사업장 관련 문의는 사업장 버튼을 눌러주세요."
    txt_Scene3_annae_4 = "연금 납부 이의신청은 지역 버튼을 눌러주세요."
    txt_Scene3_annae_1_label = Label(text = txt_Scene3_annae_1)
    txt_Scene3_annae_2_label = Label(text = txt_Scene3_annae_2)
    txt_Scene3_annae_3_label = Label(text = txt_Scene3_annae_3)
    txt_Scene3_annae_4_label = Label(text = txt_Scene3_annae_4)
    txt_Scene3_annae_1_label.place(x = 360+200, y = 200)
    txt_Scene3_annae_2_label.place(x = 360+200, y = 300)
    txt_Scene3_annae_3_label.place(x = 360+200, y = 400)
    txt_Scene3_annae_4_label.place(x = 360+200, y = 500)

    button_Scene3_ilban = Button(text = "일반상담")
    button_Scene3_saupjang = Button(text = "사업장")
    button_Scene3_jiyeok = Button(text = "지역")
    button_Scene3_ilban.place(x = 360+100, y = 600, width = 200, height = 300)
    button_Scene3_saupjang.place(x = 720+100, y = 600, width = 200, height = 300)
    button_Scene3_jiyeok.place(x = 1080+100, y = 600, width = 200, height = 300)
    
    button_Scene3_ilban.config(command = ilban)
    button_Scene3_saupjang.config(command = saupjang)
    button_Scene3_jiyeok.config(command = jiyeok)
#=====================Scene2========================
#<<<<<<<<<<<<<<<연금지급부(Scene2-1)>>>>>>>>>>>>>>>>>>
def yeonjiboo():
    txt_Scene2_annae_1_label.destroy()
    txt_Scene2_annae_2_label.destroy()
    txt_Scene2_annae_3_label.destroy()
    txt_Scene2_annae_4_label.destroy()
    button_Scene2_yeonjiboo.destroy()
    button_Scene2_daum.destroy()

    txt_Scene2_1_annae_1 = "연금지급부 창구는 나가셔서 왼쪽에 있습니다."
    txt_Scene2_1_annae_2 = "이용해 주셔서 감사합니다."
    txt_Scene2_1_annae_1_label = Label(text = txt_Scene2_1_annae_1)
    txt_Scene2_1_annae_2_label = Label(text = txt_Scene2_1_annae_2)
    txt_Scene2_1_annae_1_label.place(x = 500+150, y = 360 - 100)
    txt_Scene2_1_annae_2_label.place(x = 600+150, y = 500 - 100)

    button_yeonjiboo_cheoum = Button(text = "처음으로")
    button_yeonjiboo_cheoum.place(x = 820, y = 600, width = 200, height = 300)
    button_yeonjiboo_cheoum.config(command = win.destroy)
#<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def go_to_Scene2():
    txt_Scene1_annae_1_label.destroy()
    txt_Scene1_annae_2_label.destroy()
    button_Scene1_shinchung.destroy()
    button_Scene1_daum.destroy()

    global txt_Scene2_annae_1_label, txt_Scene2_annae_2_label, txt_Scene2_annae_3_label, txt_Scene2_annae_4_label, button_Scene2_yeonjiboo, button_Scene2_daum
    txt_Scene2_annae_1 = "연금을 수령하고 계신 경우,"
    txt_Scene2_annae_2 = "수급 계좌를 변경하시려는 경우,"
    txt_Scene2_annae_3 = "연말정산 관련 업무이신 경우 연금지급부 버튼을,"
    txt_Scene2_annae_4 = "해당하지 않는 경우 다음 버튼을 눌러주세요."
    txt_Scene2_annae_1_label = Label(text = txt_Scene2_annae_1)
    txt_Scene2_annae_2_label = Label(text = txt_Scene2_annae_2)
    txt_Scene2_annae_3_label = Label(text = txt_Scene2_annae_3)
    txt_Scene2_annae_4_label = Label(text = txt_Scene2_annae_4)
    txt_Scene2_annae_1_label.place(x = 400+200, y = 200)
    txt_Scene2_annae_2_label.place(x = 400+200, y = 300)
    txt_Scene2_annae_3_label.place(x = 400+200, y = 400)
    txt_Scene2_annae_4_label.place(x = 400+200, y = 500)

    button_Scene2_yeonjiboo = Button(text = "연금지급부")
    button_Scene2_daum = Button(text = "다음")
    button_Scene2_yeonjiboo.place(x = 580, y = 600, width = 200, height = 300)
    button_Scene2_daum.place(x = 1060, y = 600, width = 200, height = 300)
    
    button_Scene2_yeonjiboo.config(command = yeonjiboo)
    button_Scene2_daum.config(command = go_to_Scene3)
    #====================================================Scene2
#<<<<<<<<<<<<<<<<<<<<<<Scene1 branch start>>>>>>>>>>>>>>>>>>>>>>>
#----------------유족연금 안내-----------------Scene1-2
def yoojok():
    txt_Scene1_1_annae_1_label.destroy()
    txt_Scene1_1_annae_2_label.destroy()
    txt_Scene1_1_annae_3_label.destroy()
    txt_Scene1_1_annae_4_label.destroy()
    button_Scene1_1_yoojok.destroy()
    button_Scene1_1_jangae.destroy()
    button_Scene1_1_noryung.destroy()
    button_Scene1_1_banhwan.destroy()

    txt_yoojok_annae1 = "유족연금 창구는 6번입니다."
    txt_yoojok_annae2 = "번호표를 뽑고 잠깐 기다려주세요. 이용해주셔서 감사합니다."
    txt_yoojok_annae1_label = Label(text = txt_yoojok_annae1)
    txt_yoojok_annae2_label = Label(text = txt_yoojok_annae2)
    txt_yoojok_annae1_label.place(x = 600+150, y = 360 - 100)
    txt_yoojok_annae2_label.place(x = 400+150, y = 500 - 100)
    button_yoojok_cheoum = Button(text = "처음으로")
    button_yoojok_cheoum.place(x = 828, y = 600, width = 200, height = 300)
    button_yoojok_cheoum.config(command = win.destroy)
#------------------------------------------------------------
#----------------장애연금 안내-----------------Scene1-3
def jangae():
    txt_Scene1_1_annae_1_label.destroy()
    txt_Scene1_1_annae_2_label.destroy()
    txt_Scene1_1_annae_3_label.destroy()
    txt_Scene1_1_annae_4_label.destroy()
    button_Scene1_1_yoojok.destroy()
    button_Scene1_1_jangae.destroy()
    button_Scene1_1_noryung.destroy()
    button_Scene1_1_banhwan.destroy()

    txt_jangae_annae1 = "장애연금 창구는 7번입니다."
    txt_jangae_annae2 = "번호표를 뽑고 잠깐 기다려주세요. 이용해주셔서 감사합니다."
    txt_jangae_annae1_label = Label(text = txt_jangae_annae1)
    txt_jangae_annae2_label = Label(text = txt_jangae_annae2)
    txt_jangae_annae1_label.place(x = 600+150, y = 360-100)
    txt_jangae_annae2_label.place(x = 400+150, y = 500-100)

    button_jangae_cheoum = Button(text = "처음으로")
    button_jangae_cheoum.place(x = 828, y = 600, width = 200, height = 300)
    button_jangae_cheoum.config(command = win.destroy)
#------------------------------------------------------------
#----------------노령연금 안내-----------------Scene1-4
def noryung():
    txt_Scene1_1_annae_1_label.destroy()
    txt_Scene1_1_annae_2_label.destroy()
    txt_Scene1_1_annae_3_label.destroy()
    txt_Scene1_1_annae_4_label.destroy()
    button_Scene1_1_yoojok.destroy()
    button_Scene1_1_jangae.destroy()
    button_Scene1_1_noryung.destroy()
    button_Scene1_1_banhwan.destroy()

    txt_noryung_annae1 = "노령연금 창구는 8,9번입니다."
    txt_noryung_annae2 = "번호표를 뽑고 잠깐 기다려주세요. 이용해주셔서 감사합니다."
    txt_noryung_annae1_label = Label(text = txt_noryung_annae1)
    txt_noryung_annae2_label = Label(text = txt_noryung_annae2)
    txt_noryung_annae1_label.place(x = 580+150, y = 360-100)
    txt_noryung_annae2_label.place(x = 400+150, y = 500-100)

    button_noryung_cheoum = Button(text = "처음으로")
    button_noryung_cheoum.place(x = 828, y = 600, width = 200, height = 300)
    button_noryung_cheoum.config(command = win.destroy)
#------------------------------------------------------------
#----------------반환일시금 안내-----------------Scene1-5
def banhwan():
    txt_Scene1_1_annae_1_label.destroy()
    txt_Scene1_1_annae_2_label.destroy()
    txt_Scene1_1_annae_3_label.destroy()
    txt_Scene1_1_annae_4_label.destroy()
    button_Scene1_1_yoojok.destroy()
    button_Scene1_1_jangae.destroy()
    button_Scene1_1_noryung.destroy()
    button_Scene1_1_banhwan.destroy()

    txt_banhwan_annae1 = "반환일시금 창구는 5번입니다."
    txt_banhwan_annae2 = "번호표를 뽑고 잠깐 기다려주세요. 이용해주셔서 감사합니다."
    txt_banhwan_annae1_label = Label(text = txt_banhwan_annae1)
    txt_banhwan_annae2_label = Label(text = txt_banhwan_annae2)
    txt_banhwan_annae1_label.place(x = 580+150, y = 360-100)
    txt_banhwan_annae2_label.place(x = 400+150, y = 500-100)

    button_banhwan_cheoum = Button(text = "처음으로")
    button_banhwan_cheoum.place(x = 828, y = 600, width = 200, height = 300)
    button_banhwan_cheoum.config(command = win.destroy)
#--------------------------------------------------------------
#------------어떤 종류의 연금을 신청할건지 판단하는 창--------------Scene1-1
def go_to_Scene1_1():
    txt_Scene1_annae_1_label.destroy()
    txt_Scene1_annae_2_label.destroy()
    button_Scene1_shinchung.destroy()
    button_Scene1_daum.destroy()

    global txt_Scene1_1_annae_1_label ,txt_Scene1_1_annae_2_label , txt_Scene1_1_annae_3_label , txt_Scene1_1_annae_4_label , button_Scene1_1_yoojok , button_Scene1_1_jangae, button_Scene1_1_noryung , button_Scene1_1_banhwan 

    txt_Scene1_1_annae_1 = "연금 납부를 10년 이상 하신 후 연금을 신청하실 경우 노령연금 버튼을,"
    txt_Scene1_1_annae_2 = "연금 납부를 10년 미만으로 하신 후 연금을 신청하실 경우 반환일시금 버튼을,"
    txt_Scene1_1_annae_3 = "유족연금을 신청하실 경우 유족연금 버튼을,"
    txt_Scene1_1_annae_4 = "장애연금을 신청하실 경우 장애연금 버튼을 눌러주세요."
    txt_Scene1_1_annae_1_label = Label(text = txt_Scene1_1_annae_1)
    txt_Scene1_1_annae_2_label = Label(text = txt_Scene1_1_annae_2)
    txt_Scene1_1_annae_3_label = Label(text = txt_Scene1_1_annae_3)
    txt_Scene1_1_annae_4_label = Label(text = txt_Scene1_1_annae_4)
    txt_Scene1_1_annae_1_label.place(x = 400, y = 200)
    txt_Scene1_1_annae_2_label.place(x = 400, y = 300)
    txt_Scene1_1_annae_3_label.place(x = 400, y = 400) 
    txt_Scene1_1_annae_4_label.place(x = 400, y = 500)

    button_Scene1_1_noryung = Button(text = "노령연금")
    button_Scene1_1_banhwan = Button(text = "반환일시금")
    button_Scene1_1_yoojok = Button(text = "유족연금")
    button_Scene1_1_jangae = Button(text = "장애연금")
    button_Scene1_1_noryung.place(x = 400-30, y = 600, width = 200, height = 300)
    button_Scene1_1_banhwan.place(x = 700-30, y = 600, width = 200, height = 300)
    button_Scene1_1_yoojok.place(x = 1000-30, y = 600, width = 200, height = 300)
    button_Scene1_1_jangae.place(x = 1300-30, y = 600, width = 200, height = 300)


    button_Scene1_1_noryung.config(command = noryung)
    button_Scene1_1_banhwan.config(command = banhwan)
    button_Scene1_1_yoojok.config(command = yoojok)
    button_Scene1_1_jangae.config(command = jangae)
    #---------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<Scene1 branch end>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#=====================연금 신청인지 여부를 판단===============Scene1
def annae_shijak():
    txt_Scene0_annae_1_label.destroy()
    txt_Scene0_annae_2_label.destroy()
    button_annae.destroy()

    global txt_Scene1_annae_1_label, txt_Scene1_annae_2_label, button_Scene1_shinchung, button_Scene1_daum

    txt_Scene1_annae_1 = "연금을 신청하실 경우, 왼쪽의 신청 버튼을 눌러주세요."
    txt_Scene1_annae_2 = "해당하지 않는 경우, 다음을 눌러주세요."
    txt_Scene1_annae_1_label = Label(win, text = txt_Scene1_annae_1)
    txt_Scene1_annae_2_label = Label(win, text = txt_Scene1_annae_2)
    txt_Scene1_annae_1_label.place(x = 600, y = 260)
    txt_Scene1_annae_2_label.place(x = 680, y = 400)

    button_Scene1_shinchung = Button(win, text = "신청")
    button_Scene1_daum = Button(win, text = "다음")
    button_Scene1_shinchung.place(x = 580, y = 600, width = 200, height = 300)
    button_Scene1_daum.place(x = 1060, y = 600, width = 200, height = 300)


    button_Scene1_shinchung.config(command = go_to_Scene1_1)
    button_Scene1_daum.config(command = go_to_Scene2)
#=====================================================================
#=============================시작화면==================================
#--------------국민연금공단 로고, 현재 시각, 안내문과 '안내'버튼 배치------------
# img_logo_NPS = PhotoImage(file ='logo.jpeg')

img_logo_NPS_label = Label(win, text = "국민연금공단 NPS")
img_logo_NPS_label.place(x = 0, y = 0)

now = datetime.now()
txt_current_time = now.strftime('%Y-%m-%d %H:%M:%S')
current_time_label = Label(win, text = txt_current_time)
current_time_label.place(x = 1700, y = 0)

txt_Scene0_annae_1 = "어서오세요, 국민연금입니다."
txt_Scene0_annae_2 = "아래의 안내 버튼을 눌러주세요."
txt_Scene0_annae_1_label = Label(win, text = txt_Scene0_annae_1)
txt_Scene0_annae_2_label = Label(win, text = txt_Scene0_annae_2)
txt_Scene0_annae_1_label.place(x = 760, y = 260)
txt_Scene0_annae_2_label.place(x = 750, y = 400)

button_annae = Button(win, text = "안내")
button_annae.place(x = 828, y = 600, width = 200, height = 300)
button_annae.config(command = annae_shijak) #안내버튼을 누르면 안내 시작
#======================================================================
win.mainloop()
#+++++++++++++++++++++++++구현할 기능++++++++++++++++++++++++++++
#Scene1 : 연금 신청인지 아닌지 판단,
# 맞으면 노령연금/반환일시금/유족연금/장애연금 판단하는 Scene1_1로 이동
# 아니면 연금지급부 업무인지 아닌지 판단하는 Scene2로 이동
#-------------------------------------------------------
#Scene1_1 : pass
#=======================================================

#=======================================================
#Scene2 : 연금지급부 업무(기초연금, 수급계좌 변경, 연말정산)인지 아닌지 판단
# 맞으면 연금지급부 위치를 안내하는 Scene2_1로 이동
# 아니면 일반상담 창구인지를 판단하는 Scene3로 이동
#-------------------------------------------------------
#Scene2_1 : pass
#=======================================================

#=======================================================
#Scene3 : 일반상담창구 업무(서류 발급, 일반 상담)인지 아닌지 판단
# 맞으면 일반상담창구 위치를 안내하는 Scene3_1로 이동
# 아니면 사업장의 위치를 안내하는 Scene4_1로 이동

#Scene3_1 : 일반상담창구 위치 안내
#Scene4_1 : 사업장 위치 안내
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
