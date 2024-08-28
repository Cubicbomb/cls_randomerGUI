#Cube-bomb编写，屎山写法，勉强运行
'''
　　　　　　　 ┏┓       ┏┓+ +
 *　　　　　　　┏┛┻━━━━━━━┛┻┓ + +
 *　　　　　　　┃　　　　　　 ┃
 *　　　　　　　┃　　　━　　　┃ ++ + + +
 *　　　　　　 █████━█████  ┃+
 *　　　　　　　┃　　　　　　 ┃ +
 *　　　　　　　┃　　　┻　　　┃
 *　　　　　　　┃　　　　　　 ┃ + +
 *　　　　　　　┗━━┓　　　 ┏━┛
 *               ┃　　  ┃
 *　　　　　　　　　┃　　  ┃ + + + +
 *　　　　　　　　　┃　　　┃　Code is far away from bug with the animal protecting
 *　　　　　　　　　┃　　　┃ + 　　　　         神兽保佑,代码无bug
 *　　　　　　　　　┃　　　┃
 *　　　　　　　　　┃　　　┃　　+
 *　　　　　　　　　┃　 　 ┗━━━┓ + +
 *　　　　　　　　　┃ 　　　　　┣┓
 *　　　　　　　　　┃ 　　　　　┏┛
 *　　　　　　　　　┗┓┓┏━━━┳┓┏┛ + + + +
 *　　　　　　　　　 ┃┫┫　 ┃┫┫
 *　　　　　　　　　 ┗┻┛　 ┗┻┛+ + + +

'''




print('基于Tkinter的简易抽号系统，谨慎使用课堂模式。可重复单抽请多抽并抽取数量设为1。范围内抽建议多抽，抽取数量与总数相同并依次遍历择取需要的。谨慎使用课堂模式。拉大窗口开启教室后排模式。',end='\n')



from random import *
import tkinter as tk
win=tk.Tk()
win.geometry("350x400")#大小
win.title("Cb抽号系统")#标题



lst=[]
mesg=tk.StringVar()
jiwei=tk.StringVar()
mod=tk.IntVar()


def rnd():
    mood=mod.get()
    print('mod:'+str(mood))
    if mood==0:
        chou.config(state = 'normal')
        global lst,xu
        xu=0
        lst=[]
        ned=chou.get('1.0','end')#th得到
        al=zong.get('1.0','end')#th得到
        reslt.delete('1.0','end')#nt清空
        ned=int(ned)
        al=int(al)
        i=1
        if ned>al:
            print('抽号数不能大于总数')
            mesg.set("错误")
            jiwei.set("错误")
        else:
            while i<=ned:
                a=randint(1,al)
                if a in lst:
                    continue
                else:
                    print(a)
                    reslt.insert(tk.CURRENT,str(a)+',')
                    lst.append(a)
                    i=i+1
        print(lst)
        shw()
    elif mood==1:
        chou.delete('1.0','end')
        chou.insert(tk.CURRENT,'无需填写')
        al=zong.get('1.0','end')#th得到
        ned=al
        reslt.delete('1.0','end')#nt清空
        ned=int(ned)
        al=int(al)
        i=1
        reslt.insert('end',"防重复单抽模式（课堂模式）已开启")
        reslt.insert(tk.INSERT,"\n")
        while i<=ned:
            a=randint(1,al)
            if a in lst:
                continue
            else:
                lst.append(a)
                i=i+1
        reslt.insert('end',"请点击“展示”按钮","\n")
        reslt.insert(tk.INSERT,"\n")
def shw():
    mood=mod.get()
    global xu
    if mood==0:
        if xu >= len(lst):
            reslt.delete('1.0','end')
            for i in lst:
                reslt.insert(tk.CURRENT,str(i)+',')
                mesg.set("完成")
                jiwei.set("完成")
                xu=0
        else:
            s=lst[xu]
            if xu==0:
                reslt.delete('1.0','end')
                reslt.insert(tk.CURRENT,'||'+str(s)+'||'+',')
                for o in lst[xu+1:len(lst)]:
                    reslt.insert(tk.CURRENT,str(o)+',')
            elif xu==1:
                reslt.delete('1.0','end')
                i=lst[0]
                reslt.insert(tk.CURRENT,str(i)+',')
                reslt.insert(tk.CURRENT,'||'+str(s)+'||'+',')
                for o in lst[xu+1:len(lst)]:
                    reslt.insert(tk.CURRENT,str(o)+',')
            elif xu >1:
                reslt.delete('1.0','end')
                for i in lst[0:xu]:
                    reslt.insert(tk.CURRENT,str(i)+',')
                reslt.insert(tk.CURRENT,'||'+str(s)+'||'+',')
                for o in lst[xu+1:len(lst)]:
                    reslt.insert(tk.CURRENT,str(o)+',')
            mesg.set(str(s))
            jiwei.set(str(s))
            xu=xu+1
    elif mood==1:
        if xu >= len(lst):
            mesg.set("完成")
            jiwei.set("完成")
            xu=0
        s=lst[xu]
        print(s)
        reslt.insert('end',str(s)+',')
        mesg.set(str(s))
        jiwei.set(str(s))
        xu=xu+1
        
    



chou=tk.Text(win)
zong=tk.Text(win)
reslt=tk.Text(win)
bgn=tk.Button(win,text="抽取",command=rnd)
shi=tk.Button(win,text="展示",command=shw)
c=tk.Label(win,text="抽几个：")
b=tk.Label(win,text="总数：")
md=tk.Checkbutton(win, text = "课堂模式（单抽防重复）", variable=mod,onvalue=1,offvalue=0,height=5,width=20)
shu= tk.Label(win,textvariable=mesg,fg='red',font=("黑体",40))
wyx= tk.Label(win,textvariable=jiwei,fg='red',font=("黑体",400))


chou.place(x=100,y=10,width=150,height=20)#x，y是左上点坐标，w，h是宽度
zong.place(x=100,y=50,width=150,height=20)
reslt.place(x=10,y=150,width=280,height=150)
bgn.place(x=30,y=90,width=120,height=20)
shi.place(x=30,y=120,width=120,height=20)
c.place(x=50,y=10,width=50,height=20)
b.place(x=50,y=50,width=50,height=20)
shu.place(x=170,y=90)
md.place(x=30,y=300)
wyx.place(x=350,y=-80)

win.mainloop()
