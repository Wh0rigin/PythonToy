import win32gui
import win32clipboard
import win32api
import win32con
import time

title_name = '微信' #英语版则为WeChat

# 无法很好的后台需求
win = win32gui.FindWindow('WeChatMainWndForPC', title_name)
print("找到句柄：%x" % win)
if win != 0:
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(left, top, right, bottom)
    print(right - left, bottom - top)
    win32gui.SetForegroundWindow(win)
else:
    print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)


def sendMSG(str1):

    
    #微信无法很好的使用clipboard
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str1)
    win32clipboard.CloseClipboard()

    zhanTie()

    huiche()

    #win32api.SendMessage(win, win32con.WM_PASTE, 0, 0)
    #win32api.PostMessage(win, win32con.WM_PASTE, 0, 0)
    
    #win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    
    print(time.asctime(time.localtime(time.time()))[11:-5]+'发送成功:'+str1)

def zhanTie():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

def huiche():
    win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
    win32api.keybd_event(83, 0, 0, 0)  # s键位码
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)

msg = input("请输入要发送的数据：")
delay = input("请设置延时：")
while True:
    
    sendMSG('本地时间:'+time.asctime(time.localtime(time.time()))[11:-5]+':'+ msg)
    time.sleep(int(delay))
