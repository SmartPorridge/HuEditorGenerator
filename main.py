#!/usr/bin/python
# -*- coding: UTF-8 -*-

from hu_style_sentenses import get_Hu_style_sentenses
# import os, re
import random
import tkinter as tk
import hu_style_sentenses
# import webbrowser
from PIL import Image, ImageTk
from memory_pic import *
import base64,os


# def 读JSON文件(fileName=""):
#     import json
#     if fileName!='':
#         strList = fileName.split(".")
#         if strList[len(strList)-1].lower() == "json":
#             with open(fileName,mode='r',encoding="utf-8") as file:
#                 return json.loads(file.read())

class HuStyle:
    def __init__(self):
        # data = 读JSON文件("老胡语料.json")
        data = get_Hu_style_sentenses() 
        self.名人名言 = data["famous"] # 主要取自老胡经典的话
        self.前面垫话 = data["before"] # 在老胡名言前面弄点话
        self.后面垫话 = data['after']  # 在老胡名言后面弄点话
        self.废话 = data['bosh'] # 老胡文章主要废话
        self.重复度 = 2

    def 洗牌遍历(self,列表):
        # global 重复度
        池 = list(列表) * self.重复度
        while True:
            random.shuffle(池)
            for 元素 in 池:
                yield 元素

    def 来点名人名言(self):
        # global 下一句名人名言
        xx = next(self.洗牌遍历(self.名人名言))
        xx = xx.replace(  "a",random.choice(self.前面垫话) )
        xx = xx.replace(  "b",random.choice(self.后面垫话) )
        return xx

    def 另起一段(self):
        xx = "。"
        xx += "\r\n"
        xx += " "
        return xx

    def generate_Hu_style_article(self):
            """生成胡编风格的文章"""
            global article_var
            global author_Entry # 老胡
            global topic_Entry  
            global paragraph_Entry # 5
            global per_paragraph_num_max_Entry # 100
            global article_text

            xx = topic_Entry.get()
            author = author_Entry.get()
            # print(xx)
            
            final_article = ''
            for index in range(int(paragraph_Entry.get())):
                # print(x)
                tmp = str()
                while ( len(tmp) < int(per_paragraph_num_max_Entry.get()) ) :
                    分支 = random.randint(0,50)
                    if 分支 < 10:
                        tmp += self.另起一段()
                    elif 分支 < 25 :
                        tmp += self.来点名人名言()
                    else:
                        tmp += next(self.洗牌遍历(self.废话))
                tmp = tmp.replace("x",xx).replace("。。", "。").replace("，，", "，").replace("，。", "。").replace("？。", "？").replace('\n','')
                tmp = tmp.replace('老胡',author)
                if tmp.startswith('。'):
                    tmp = tmp[1:]
                tmp = r"    " + tmp + '\n'
                # print(tmp)
                if not tmp == '。':
                    final_article += tmp

            article_var.set(final_article)
            article_text.delete(1.0, "end")
            article_text.insert('insert',final_article)
            # print(final_article)


if __name__ == "__main__":
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    
    # 第2步，给窗口的可视化起名字
    window.title('胡编乱造生成器V1.0')
    
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('1000x800')  # 这里的乘是小x

    # 第4步，在图形界面上创建一个标签用以显示内容并放置
    w = tk.Label(window, text='欢迎使用胡编乱造生成器', width=30, height=1, fg='Firebrick', font=('黑体', 24))  
    # w.pack()
    w.pack(fill=tk.X,pady=15)
    # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成
    
    # 第5步，创建一个主frame，长在主window窗口上
    frame = tk.Frame(window)
    frame.pack()
    
    # 第6步，创建第二层框架frame，长在主框架frame上面
    frame_l = tk.Frame(frame)# 第二层frame，左frame，长在主frame上
    frame_r = tk.Frame(frame)# 第二层frame，右frame，长在主frame上
    frame_l.pack(side='left')
    frame_r.pack(side='right')

    # 添加第三层 frame ，为图片留下空间
    frame_r_r = tk.Frame(frame_r)
    frame_r_r.pack(side='right')
    frame_r_l = tk.Frame(frame_r)
    frame_r_l.pack(side='left')

    # 第7步，创建标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
    tk.Label(frame_l, text='请输入作者名字：',font=('Arial', 14)).pack() # author
    tk.Label(frame_l, text='请输入生成话题：', font=('Arial', 14)).pack() # topic  
    tk.Label(frame_l, text='生成段落数(如:5)：',font=('Arial', 14)).pack() # paragraph
    tk.Label(frame_l, text='每段字数(如:100)：', font=('Arial', 14)).pack() #
    
    author_txt = tk.StringVar()
    author_txt.set("老胡")
    author_Entry = tk.Entry(frame_r_l, show=None, textvariable=author_txt, fg="gray", font=('Arial', 14))
    author_Entry.pack(padx=60)

    topic_txt = tk.StringVar()
    topic_txt.set("吴亦凡被锤")
    topic_Entry = tk.Entry(frame_r_l, show=None, textvariable=topic_txt, fg="gray", font=('Arial', 14))
    topic_Entry.pack()

    paragraph_num = tk.StringVar()
    paragraph_num.set("5")
    paragraph_Entry = tk.Entry(frame_r_l, show=None, textvariable=paragraph_num, fg="gray", font=('Arial', 14))
    paragraph_Entry.pack()

    per_paragraph_num_max = tk.StringVar()
    per_paragraph_num_max.set("100")
    per_paragraph_num_max_Entry = tk.Entry(frame_r_l, show=None, textvariable=per_paragraph_num_max, fg="gray", font=('Arial', 14))
    per_paragraph_num_max_Entry.pack()
    

    # # 放个图片 二维码
    # 读图片
    # image1 = Image.open("QR_arxivdaily.jpg").resize((80, 80),0)
    # 从.py文件中读取图片
    image1 = open("tmp_qr_code.jpg", 'wb')
    image1.write(base64.b64decode(QR_arxivdaily_jpg))
    image1.close()
    image1 = Image.open("tmp_qr_code.jpg").resize((80, 80),0)
    #删除临时图片
    os.remove('tmp_qr_code.jpg')

    photo = ImageTk.PhotoImage(image1)
    w_photo = tk.Label(frame_r_r, text = "扫码关注公众号\n回复“胡编乱造”获取本软件源代码",compound = 'top',image=photo)
    w_photo.pack(side='right',)


    article_var = tk.StringVar()
    HU = HuStyle()
    # 设置'生成文章'按钮
    generate_b = tk.Button(window, text='生成文章', font=('黑体', 19), width=10, height=1,relief='groove',fg='White', bg='LightSeaGreen',command=HU.generate_Hu_style_article)
    generate_b.pack()
    # generate_b.pack(fill=tk.X,padx=180,pady=10)
    

    warning = tk.Label(window, text='警告！仅供娱乐，禁止用于其他任何场合！语料库来源于网络，不代表作者立场！',fg='red',font=('宋体', 13))
    warning.pack(pady=2) 
    # 一切滥用使用后果自负！
    # 好用，第4步，在图形界面上显示文本框
    # article_lb = tk.Label(window, textvariable=article_var, bg='white', fg='black', font=('楷体', 13),justify="left",wraplength=900)
    # # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    # article_lb.pack(padx=15,pady=15)

    # article_text = tk.Text(window, width='30', height='10')
    article_text = tk.Text(window, width='90', height='23',font=('楷体', 15))
    article_text.pack()

    # # 设置label标签
    # link = tk.Label(window, text='GitHub源代码', font=('Arial', 10, 'underline'))
    # link.pack()
    
    # # 此处必须注意，绑定的事件函数中必须要包含event参数
    # def open_url(event):
    #     webbrowser.open("https://github.com/mediatoreditor/HuEditorGenerator", new=0)
    
    # # 绑定label单击时间
    # link.bind("<Button-1>", open_url)


    tk.Label(window, text='Author：Mr.Green   Copyright (c) 2021\nAnti 996 License Version 1.0 (Draft)',fg='gray',font=('Arial', 9)).pack() # author

    # 主窗口循环显示
    window.mainloop()