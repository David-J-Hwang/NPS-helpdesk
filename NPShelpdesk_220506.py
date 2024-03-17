# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.font import *

win = Tk()
win.geometry("1280x720")
win.title("안내프로그램_국민연금공단 남울산지사")
win.option_add("*Font", "궁서 23")

# nps_logo = "yelcrys/Desktop/Python_tkinter/logo_NPS.png"
# nps_logo_image = PhotoImage(file = nps_logo)
# nps_logo_label = Label(win, image = nps_logo_image)
# nps_logo_label.pack()

nps_logo = Label(win, text = "NPS 국민연금공단")
nps_logo.place(relx = 0, rely = 0)

#======Scene 0(대기화면)=========
def win_exit():
    win.destroy()

def annae_shijak():
    #Scene0 초기화
    scene0_text1.destroy()
    scene0_text2.destroy()
    scene0_annae.destroy()
    #Scene1로 넘기기
    scene1_text1 = Label(win, text = "연금을 신청하실 경우, 왼쪽의 신청 버튼을 눌러주세요.")
    scene1_text1.place(relx = 0.35, rely = 0.23)
    scene1_text2 = Label(win, text = "해당하지 않는 경우, 다음을 눌러주세요.")
    scene1_text2.place(relx = 0.4, rely = 0.33)
    scene1_apply = Button(win, text = "신청")
    scene1_apply.place(relx = 0.2, rely = 0.9)
    #scene1_apply.config(command = pension_apply) #Scene1-1 연금신청 페이지 로드
    scene1_next = Button(win, text = "다음")
    scene1_next.place(relx = 0.8, rely = 0.9)
    #scene1_next.config(command = Scene2)
    #Scene2 : 연금지급부 확인 여부 페이지 로드
    scene1_exit = Button(win, text = "종료")
    scene1_exit.place(relx = 0.5, rely = 0.9)
    scene1_exit.config(command = win_exit)

annae_fontStyle = Font(family = "Lucida Grande", size = 23)

scene0_text1 = Label(win, text  = "어서오세요, 국민연금입니다.")
scene0_text1.place(relx = 0.41, rely = 0.2)
scene0_text2 = Label(win, text = "아래의 안내 버튼을 눌러주세요.")
scene0_text2.place(relx = 0.4, rely = 0.3)

scene0_annae = Button(win, text = "안내")
scene0_annae.place(relx = 0.48, rely = 0.9)
scene0_annae.config(command = annae_shijak)

win['bg'] = '#FFFFFF'
win.mainloop()