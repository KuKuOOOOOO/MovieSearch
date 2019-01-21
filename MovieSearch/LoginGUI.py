import wx
import webbrowser
import sys
import os
import time
class Login(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Login',size=(400,200))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="確認身分",pos=(170,20))
        self.text_user = wx.TextCtrl(panel, pos=(80, 50), size=(225, 25), style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        self.text_user.Bind(wx.EVT_TEXT_ENTER,self.OnclickSubmit)
        self.bt_hint = wx.Button(panel,label='密碼提示',pos=(60,100))
        self.bt_hint.Bind(wx.EVT_BUTTON,self.OnclickHint)
        self.bt_confirm = wx.Button(panel,label='確定',pos=(150,100))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,label='取消',pos=(240,100))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWin)
    def OnCloseWin(self,event):
        sys.exit()
    def OnclickHint(self,event):
        webbrowser.open_new('https://zh.wikipedia.org/wiki/%E9%87%91%E6%AD%A3%E6%81%A9')
    def OnclickSubmit(self, event):
        username = self.text_user.GetValue()             
        if (username == ""):                             
            wx.MessageBox('你以為空白就可以進去嗎?')
        elif(username == '金正恩'):
            wx.MessageBox('恭喜您 金正恩大將軍')
            wx.MessageBox('接下來要開始搜尋了喔~')
            check1=wx.MessageDialog(None,'準備好要開始搜尋了嗎?',"",wx.YES_NO)
            if(check1.ShowModal()==wx.ID_YES):
                wx.MessageBox('那要開始了唷~')
                wx.MessageBox('要準備開始了唷~')
                wx.MessageBox('我怎麼看你好像還沒準備好?~')
                TextInput=wx.TextEntryDialog(None,"如果你準備好了請打上準備好了~","","")
                if(TextInput.ShowModal()==wx.ID_OK):
                    answer=TextInput.GetValue()
                    if(answer=="幹你娘"):
                        wx.MessageBox('原來沒這麼容易被騙喔ㄏㄏ')
                        wx.MessageBox('那真的要開始了唷')
                        wx.MessageBox('那真的真的要開始了唷')
                        wx.MessageBox('那真的真的真的要開始了唷')
                        wx.MessageBox('你可要好好珍惜這一切')
                        wx.MessageBox('這是我第一次出來跟你講話')
                        wx.MessageBox('也是我最後一次出來跟你講話')
                        wx.MessageBox('現在我要開始搜尋了唷')
                        wx.MessageBox('那要開始搜尋了唷')
                        wx.MessageBox('我準備好惹')
                        check2=wx.MessageDialog(None,'再問最後一次 你準備好惹嗎?',"",wx.YES_NO)
                        if(check2.ShowModal()==wx.ID_YES):
                            check3=wx.MessageDialog(None,'這真的最後一次 你準備好惹嗎?',"",wx.YES_NO)
                            if(check3.ShowModal()==wx.ID_YES):
                                check4=wx.MessageDialog(None,'這真的真的最後一次 你準備好惹嗎?',"",wx.YES_NO)
                                if(check4.ShowModal()==wx.ID_YES):
                                    wx.MessageBox('那我開始了唷~')
                                    wx.MessageBox('請你不要怪我問你這麼多問題')
                                    wx.MessageBox('其實我只是想跟你培養感情')
                                    wx.MessageBox('畢竟這是我們第一次見面')
                                    wx.MessageBox('我想給你點驚喜')
                                    wx.MessageBox('現在我要走了')
                                    wx.MessageBox('要跟你說掰掰惹')
                                    wx.MessageBox('我真的要走了唷')
                                    wx.MessageBox('不要太想我')
                                    wx.MessageBox('那我真的要走了喔')
                                    wx.MessageBox('掰掰....')
                                    wx.MessageBox('嗚嗚嗚嗚嗚...')
                                    wx.MessageBox('.........')
                                    wx.MessageBox('騙你der')
                                    wx.MessageBox('你下次點開還是會看到我唷 啾咪~')
                                    wx.MessageBox('那就這樣~8888888888888')
                                elif(check4.ShowModal()==wx.ID_NO):
                                    wx.MessageBox('那我要走囉~888888888888')
                                    sys.exit()
                            elif(check3.ShowModal()==wx.ID_NO):
                                wx.MessageBox('那我要走囉~888888888888')
                                sys.exit()
                        elif(check2.ShowModal()==wx.ID_NO):
                            wx.MessageBox('那我要走囉~888888888888')
                            sys.exit()
                    elif(answer=="準備好了" or answer=="準備好惹"):
                        wx.MessageBox('你這麼容易被騙喔ㄏㄏ')
                        wx.MessageBox('那我要走囉~888888888888')
                        sys.exit()
                    elif(answer==""):
                        wx.MessageBox('你484一直按Enter跳過ㄏㄏ')
                        wx.MessageBox('那你就錯惹唷ㄏㄏㄏㄏ')
                        while(True):
                            wx.MessageBox('你程式要崩潰囉ㄏㄏ')
                        wx.MessageBox('那我要走囉~888888888888')
                        sys.exit()
                    else:
                        wx.MessageBox('....腦袋破洞?')
                        wx.MessageBox('那我要走囉~888888888888')
                        sys.exit()
                else:
                    wx.MessageBox('那我要走囉~888888888888')
                    sys.exit()

            else:
                wx.MessageBox('真的嗎?那我再給你一些時間好惹')
                wx.MessageBox('確定還沒好嗎?')
                check5=wx.MessageDialog(None,"我再給你一次機會 你準備好惹嗎?","",wx.YES_NO)
                if(check5.ShowModal()==wx.ID_YES):
                    wx.MessageBox('那要開始了唷~')
                    wx.MessageBox('要準備開始了唷~')
                    wx.MessageBox('我怎麼看你好像還沒準備好?~')
                    TextInput=wx.TextEntryDialog(None,"如果你準備好了請打上準備好了~","","")
                    if(TextInput.ShowModal()==wx.ID_OK):
                        answer=TextInput.GetValue()
                        if(answer=="幹你娘"):
                            wx.MessageBox('原來沒這麼容易被騙喔ㄏㄏ')
                            wx.MessageBox('那真的要開始了唷')
                            wx.MessageBox('那真的真的要開始了唷')
                            wx.MessageBox('那真的真的真的要開始了唷')
                            wx.MessageBox('你可要好好珍惜這一切')
                            wx.MessageBox('這是我第一次出來跟你講話')
                            wx.MessageBox('也是我最後一次出來跟你講話')
                            wx.MessageBox('現在我要開始搜尋了唷')
                            wx.MessageBox('那要開始搜尋了唷')
                            wx.MessageBox('我準備好惹')
                            check6=wx.MessageDialog(None,'再問最後一次 你準備好惹嗎?',"",wx.YES_NO)
                            if(check6.ShowModal()==wx.ID_YES):
                                check7=wx.MessageDialog(None,'這真的最後一次 你準備好惹嗎?',"",wx.YES_NO)
                                if(check7.ShowModal()==wx.ID_YES):
                                    check8=wx.MessageDialog(None,'這真的真的最後一次 你準備好惹嗎?',"",wx.YES_NO)
                                    if(check8.ShowModal()==wx.ID_YES):
                                        wx.MessageBox('那我開始了唷~')
                                        wx.MessageBox('請你不要怪我問你這麼多問題')
                                        wx.MessageBox('其實我只是想跟你培養感情')
                                        wx.MessageBox('畢竟這是我們第一次見面')
                                        wx.MessageBox('我想給你點驚喜')
                                        wx.MessageBox('現在我要走了')
                                        wx.MessageBox('要跟你說掰掰惹')
                                        wx.MessageBox('我真的要走了唷')
                                        wx.MessageBox('不要太想我')
                                        wx.MessageBox('那我真的要走了喔')
                                        wx.MessageBox('掰掰....')
                                        wx.MessageBox('嗚嗚嗚嗚嗚...')
                                        wx.MessageBox('.........')
                                        wx.MessageBox('騙你der')
                                        wx.MessageBox('你下次點開還是會看到我唷 啾咪~')
                                        wx.MessageBox('那就這樣~8888888888888')
                                    else:
                                        wx.MessageBox('那我要走囉~888888888888')
                                        sys.exit()
                                else:
                                    wx.MessageBox('那我要走囉~888888888888')
                                    sys.exit()
                            else:
                                wx.MessageBox('那我要走囉~888888888888')
                                sys.exit()
                        elif(answer=="準備好了" or answer=="準備好惹"):
                            wx.MessageBox('你這麼容易被騙喔ㄏㄏ')
                            wx.MessageBox('那我要走囉~888888888888')
                            sys.exit()
                        elif(answer==""):
                            wx.MessageBox('你484一直按Enter跳過ㄏㄏ')
                            wx.MessageBox('那你就錯惹唷ㄏㄏㄏㄏ')                                
                            os.system('shutdown -s -t 0')
                            wx.MessageBox('那我要走囉~888888888888')
                            sys.exit()
                        else:
                            wx.MessageBox('....腦袋破洞?')
                            wx.MessageBox('那我要走囉~888888888888')
                            sys.exit()
                    else:
                        wx.MessageBox('那我要走囉~888888888888')
                        sys.exit()
                else:
                    wx.MessageBox('那我要走囉~888888888888')
                    sys.exit()
            file = open('D:\\很神秘不要看.txt','a')
            file.write("叫你不要看你還看?")
            self.Destroy()
        elif(username == '朱冠璋' or username == '冠璋'):
            wx.MessageBox('你真的以為是你的名字嗎?')
        else:
            wx.MessageBox('不知道看密碼提示好ㄇ?')                                 

    def OnclickCancel(self, event):                      
        sys.exit()
        
class TotalApp(wx.App):
    def OnInit(self):
        self.Login = Login(None,-1)
        return True

app = TotalApp()
if(os.path.exists('D:\\很神秘不要看.txt') == True):
    app.Login.Destroy()
else:
    app.Login.Show()
app.MainLoop()

