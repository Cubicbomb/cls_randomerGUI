# Cube-bomb编写，屎山写法，勉强运行

# 基于Tkinter的简易抽号系统使用说明
print('基于Tkinter的简易抽号系统，谨慎使用课堂模式。可重复单抽请多抽并抽取数量设为1。范围内抽建议多抽，抽取数量与总数相同并依次遍历择取需要的。谨慎使用课堂模式。拉大窗口开启教室后排模式。', end='\n')

# 导入随机模块和tkinter模块
from random import *
import tkinter as tk

# 创建Tkinter窗口对象
win = tk.Tk()
win.geometry("350x400")  # 设置窗口大小
win.title("Cb抽号系统")  # 设置窗口标题

# 初始化列表和字符串变量
rdlist = []
mesg = tk.StringVar()
jiwei = tk.StringVar()
mod = tk.IntVar()

# 定义抽取号码的函数
def rnd():
    _mod = mod.get()
    print('mod:' + str(_mod))
    if _mod == 0:# 普通模式
        chou.config(state='normal')
        global rdlist, xu
        rdlist = []
        ned = chou.get('1.0', 'end')  # 获取抽取数量
        al = zong.get('1.0', 'end')  # 获取总数
        reslt.delete('1.0', 'end')  # 清空结果框
        ned = int(ned)
        al = int(al)
        i = 1
        if ned > al:
            print('抽号数不能大于总数')
            mesg.set("错误")
            jiwei.set("错误")
            reslt.insert(tk.CURRENT, "【错误】抽号数不能大于总数")
        else:
            while i <= ned:
                a = randint(1, al)
                if a in rdlist:
                    continue
                else:
                    #print(a)
                    reslt.insert(tk.CURRENT, str(a) + ',')#插入文字
                    rdlist.append(a)
                    i = i + 1
            #print(rdlist)
            print("本次抽取完毕,点按“展示”逐一高亮展示抽取结果")
            #准备接入展示函数shw()初始化
            xu = 0
            reslt.mark_set(tk.INSERT,'1.0')
            shw()# 接入展示结果
    elif _mod == 1:
        chou.delete('1.0', 'end')
        chou.insert(tk.CURRENT, '无需填写')
        chou.config(state='disabled')
        al = zong.get('1.0', 'end')  # 获取总数
        ned = al
        reslt.delete('1.0', 'end')  # 清空结果框
        ned = int(ned)
        al = int(al)
        i = 1
        reslt.insert('end', "防重复单抽模式（课堂模式）已开启")
        reslt.insert(tk.INSERT, "\n")
        while i <= ned:
            a = randint(1, al)
            if a in rdlist:
                continue
            else:
                rdlist.append(a)
                i = i + 1
        reslt.insert('end', "请点击“展示”按钮", "\n")
        reslt.insert(tk.INSERT, "\n")


def shw():
    _mod = mod.get()
    global xu, pre_s

    if not isinstance(rdlist, list) or not rdlist:
        return

    if _mod == 0:
        if xu >= len(rdlist):
            #reslt.tag_delete("precheckment")
            reslt.tag_delete("nowcheckment")
            mesg.set("完成")
            jiwei.set("完成")
            xu = 0
            reslt.mark_set(tk.INSERT, "1.0")
            return

        #reslt.tag_config("precheckment", background=reslt.cget('background'), foreground="blue", underline=0)
        reslt.tag_config("nowcheckment", background="yellow", foreground="red", underline=1)

        s = rdlist[xu]
        s_str = str(s)
        length = len(s_str) + 1

        current_index = reslt.index(tk.INSERT)

        #if xu != 0:
            #prev_index = f"{current_index}-{(len(str(pre_s)) + 1)}c"
            #reslt.tag_add("precheckment", prev_index, current_index)

        reslt.tag_add("nowcheckment", current_index, f"{current_index}+{length}c")
        reslt.mark_set(tk.INSERT, f"{current_index}+{length}c")
        reslt.see(tk.INSERT)

        mesg.set(s_str)
        jiwei.set(s_str)
        pre_s = s
        xu += 1

    elif _mod == 1:
        if xu >= len(rdlist):
            mesg.set("完成")
            jiwei.set("完成")
            xu = 0
            return

        s = rdlist[xu]
        s_str = str(s)

        reslt.insert('end', s_str + ',')
        mesg.set(s_str)
        jiwei.set(s_str)
        xu += 1


# 创建Tkinter控件
chou = tk.Text(win)
zong = tk.Text(win)
reslt = tk.Text(win)
bgn = tk.Button(win, text="抽取", command=rnd)
shi = tk.Button(win, text="展示", command=shw)
c = tk.Label(win, text="抽几个：")
b = tk.Label(win, text="总数：")
md = tk.Checkbutton(win, text="课堂模式（单抽防重复）", variable=mod, onvalue=1, offvalue=0, height=5, width=20)
shu = tk.Label(win, textvariable=mesg, fg='red', font=("黑体", 40))
wyx = tk.Label(win, textvariable=jiwei, fg='red', font=("黑体", 400))

# 布局Tkinter控件
chou.place(x=100, y=10, width=150, height=20)  # x，y是左上点坐标，w，h是宽度
zong.place(x=100, y=50, width=150, height=20)
reslt.place(x=10, y=150, width=280, height=150)
bgn.place(x=30, y=90, width=120, height=20)
shi.place(x=30, y=120, width=120, height=20)
c.place(x=50, y=10, width=50, height=20)
b.place(x=50, y=50, width=50, height=20)
shu.place(x=170, y=90)
md.place(x=30, y=300)
wyx.place(x=350, y=-80)

# 运行Tkinter事件循环
win.mainloop()