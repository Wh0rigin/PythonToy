import win32gui
import win32clipboard
import win32api
import win32con
import time

title_name = '哔哩哔哩直播，二次元弹幕直播平台 - Google Chrome'


win = win32gui.FindWindow('Chrome_WidgetWin_1', title_name)
print("找到句柄：%x" % win)
if win != 0:
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(left, top, right, bottom)
    print(right - left, bottom - top)
    win32gui.SetForegroundWindow(win)
else:
    print('请注意：找不到【%s】，请激活窗口！' % title_name)


def sendMSG(str1):
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str1)
    win32clipboard.CloseClipboard()

    zhanTie()

    #huiche()

    #win32api.SendMessage(win, win32con.WM_PASTE, 0, 0)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


    print('本地时间:'+time.asctime(time.localtime(time.time()))[11:-5]+':'+ str1)

def zhanTie():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

msg = input("请输入要发送的数据：")
delay = input("请设置延时：")
while True:
    
    sendMSG(msg)
    time.sleep(int(delay))


