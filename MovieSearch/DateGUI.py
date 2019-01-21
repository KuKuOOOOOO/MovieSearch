import wx
import LoginGUI
import datetime
from datetime import timedelta
import sys
CheckDate = 0
class DateGUi(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Date',size=(400,200))
        panel = wx.Panel(self)
        nowTime = datetime.datetime.today()
        ThisWeekStart = nowTime - timedelta(days=nowTime.weekday())
        ThisWeekEnd = nowTime + timedelta(days=6 - nowTime.weekday())
        ThisWeekStartStr = ThisWeekStart.strftime("%Y-%m-%d")
        ThisWeekEndStr = ThisWeekEnd.strftime("%Y-%m-%d")
        WeekRange = ThisWeekStartStr + "~" + ThisWeekEndStr
        self.title = wx.StaticText(panel,label = "請選擇電影大概上映日期",pos = (130,20))
        self.nowTime = wx.StaticText(panel,label = "本周日期:" + WeekRange,pos = (100,40))
        self.ThisWeek = wx.Button(panel,label = '本周上映',pos = (100,60))
        self.ThisWeek.Bind(wx.EVT_BUTTON, self.ClickThisWeek)
        self.OtherWeek = wx.Button(panel,label="本周以外上映",pos=(200,60))
        self.OtherWeek.Bind(wx.EVT_BUTTON, self.ClickOther)
        self.description = wx.Button(panel,label="看不懂按這裡好ㄇ",pos=(135,90))
        self.description.Bind(wx.EVT_BUTTON, self.ClickDescription)
    def ClickDescription(self, event):
        option = wx.MessageBox("你看不懂?你484登能兒?",style=wx.YES_NO)
        if(option == wx.YES):
            wx.MessageBox("本周上映之電影請點選\"本周上映\"\n其他則點選\"本周以外上映\"")
        elif(option == wx.NO):
            wx.MessageBox("那你按這個是在按三小?")
    def ClickThisWeek(self,event):
        global CheckDate
        CheckDate = 1
        self.Destroy()
    def ClickOther(self,event):
        global CheckDate
        CheckDate = 2
        self.Destroy()
    def ThisWeekOrOther():
        if(CheckDate == 1):
            Yahoo_URL = 'https://movies.yahoo.com.tw/movie_thisweek.html'
        elif(CheckDate==2):
            Yahoo_URL = 'https://movies.yahoo.com.tw/movie_intheaters.html?page=1'
        else:
            sys.exit()
        return Yahoo_URL
class TotalApp(wx.App):
    def OnInit(self):
        self.DateGUi = DateGUi(None,-1)
        return True

app = TotalApp()
app.DateGUi.Show()
app.MainLoop()
