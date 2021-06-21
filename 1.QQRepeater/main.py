import win32gui
import win32clipboard
import win32api
import win32con
import time

title_name = '不是龙王是龙神'


win = win32gui.FindWindow('TXGuiFoundation', title_name)
print("找到句柄：%x" % win)
if win != 0:
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(left, top, right, bottom)
    print(right - left, bottom - top)
    win32gui.SetForegroundWindow(win)
else:
    print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)


def sendMSG(str1):
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, str1)
    win32clipboard.CloseClipboard()


    win32api.SendMessage(win, win32con.WM_PASTE, 0, 0)
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    print(time.asctime(time.localtime(time.time()))[11:-5]+'发送成功:'+str1)

msg = input("请输入要发送的数据：")
delay = input("请设置延时：")
while True:
    
    sendMSG('本地时间:'+time.asctime(time.localtime(time.time()))[11:-5]+':'+ msg)
    time.sleep(int(delay))

