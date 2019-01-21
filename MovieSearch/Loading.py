import wx
from wx.adv import Animation, AnimationCtrl
import DateGUI
class Loading(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,size=(400,200),style=0)
        panel = wx.Panel(self)
        self.LoadingText = wx.StaticText(panel,label="Loading...",pos=(335,20))
        self.LoadingText.SetForegroundColour('white') 
        sizer = wx.BoxSizer(wx.VERTICAL)
        anim = Animation('123.gif')
        ctrl = AnimationCtrl(self,id,anim)
        #ctrl.Play()
        sizer.Add(ctrl)
        self.SetSizerAndFit(sizer)
class TotalApp(wx.App):
    def OnInit(self):
        self.Loading = Loading(None,-1)
        return True
app=TotalApp()
app.Loading.Show()
app.MainLoop()