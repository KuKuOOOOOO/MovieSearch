import wx
import re
import os
import sys
import YahooMovie

class MainForm(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'MovieSearch',size=(800,500))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="輸入你記得的電影名稱",pos=(335,20))
        self.SearchText = wx.TextCtrl(panel, pos=(280, 50), size=(225, 25), style=wx.TE_LEFT | wx.TE_PROCESS_ENTER)
        self.SearchText.Bind(wx.EVT_TEXT_ENTER,self.OnclickSubmit)
        self.bt_confirm = wx.Button(panel,label='確定',pos=(350,100))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.MoiveName = wx.StaticText(panel,label="",pos=(150,150))
        self.Taps = wx.StaticText(panel,label="",pos=(150,180))
        self.Theater = wx.StaticText(panel,label="",pos=(150,210),size=(1000,100))
        self.Times = wx.StaticText(panel,label="",pos=(150,240),size=(1000,100))
        self.Bind(wx.EVT_CLOSE,self.OnCloseWin)
        self.Attention=wx.StaticText(panel,label="其他電影院相關時刻即開啟MoiveData.xls可觀看並請留意關閉程式時會將MovieData.xls刪除",pos=(150,400),size=(1000,100))
    def OnCloseWin(self,event):
        if(os.path.exists('MovieData.xls')):
            os.remove('MovieData.xls')
            sys.exit()
        else:
            sys.exit()
    def OnclickSubmit(self, event):
        MovieName = self.SearchText.GetValue()
        #判斷Excel是否有任何電影
        if(YahooMovie.Read_Excel(1,2)==""):
            self.Theater.SetLabel("\t\t\t" + "這周的電影還沒上映or還沒有時刻表")
        else:
            for i in range(0,len(YahooMovie.Theater_DB),1):
                ExcelRead_Name = YahooMovie.Read_Excel(i,0)
                ExcelRead_Date = YahooMovie.Read_Excel(i,1)
                re_ExcelReadName = re.findall('.\w',str(ExcelRead_Name))
                #判斷搜尋字是否為空白
                if(MovieName != ""):
                    try:
                        #判斷是否有搜尋到KeyWord
                        if(MovieName in re_ExcelReadName[0] or MovieName in re_ExcelReadName[1] or MovieName in re_ExcelReadName[2] or MovieName in re_ExcelReadName[3]):
                            print(ExcelRead_Name + '\t' + ExcelRead_Date)
                            print('---------------------------------------------')
                            self.MoiveName.SetLabel(ExcelRead_Name)
                            for j in range(i,len(YahooMovie.Theater_DB),1):
                                ExcelRead_Theater = YahooMovie.Read_Excel(j,3)
                                ExcelRead_Taps = YahooMovie.Read_Excel(j,2)
                                ExcelRead_Times = YahooMovie.Read_Excel(j,4)
                                if(ExcelRead_Theater == '親親數位影城'):                  #判斷是否為我要的電影院
                                    print(ExcelRead_Taps + '\t' + ExcelRead_Theater + '\t' + ExcelRead_Times)
                                    self.Taps.SetLabel(ExcelRead_Taps)
                                    self.Theater.SetLabel(ExcelRead_Theater)
                                    self.Times.SetLabel(ExcelRead_Times)
                                    break
                                elif(YahooMovie.Read_Excel(j,2) == "台中的電影院沒有撥~"):#判斷台中有沒有電影院
                                    print('台中的電影院沒有撥~')
                                    self.Taps.SetLabel("")
                                    self.Theater.SetLabel("台中的電影院沒有撥~")
                                    self.Times.SetLabel("")
                                    break
                                elif(YahooMovie.Read_Excel(j + 1,1) != "" and YahooMovie.Read_Excel(j + 1,3) == "親親數位影城"):#判斷是否該電影下一行是否有電影及我要的電影院
                                    print("親親沒有啦ㄏㄏ")
                                    self.Taps.SetLabel("")
                                    self.Theater.SetLabel("親親沒有啦ㄏㄏ")
                                    self.Times.SetLabel("")
                                    break
                                elif(YahooMovie.Read_Excel(j,1) != "" and i != j):                                 #判斷是否為該電影之最後一個電影院
                                    print("親親沒有啦ㄏㄏ")
                                    self.Taps.SetLabel("")
                                    self.Theater.SetLabel("親親沒有啦ㄏㄏ")
                                    self.Times.SetLabel("")
                                    break
                                elif(j == len(YahooMovie.Theater_DB) - 1 and ExcelRead_Theater != '親親數位影城'):#判斷最後一個是否為我要的電影院
                                    print("親親沒有啦ㄏㄏ")
                                    self.Taps.SetLabel("")
                                    self.Theater.SetLabel("親親沒有啦ㄏㄏ")
                                    self.Times.SetLabel("")
                            break
                        elif(i == len(YahooMovie.Theater_DB) - 1 and ExcelRead_Name != MovieName):#判斷Excel裡是否有資料
                            print('這網頁還沒有這個電影的時刻表ㄏㄏ')
                            self.MoiveName.SetLabel("")
                            self.Taps.SetLabel("")
                            self.Theater.SetLabel("\t\t\t" + "這網頁還沒有這個電影的時刻表ㄏㄏ")
                            self.Times.SetLabel("")
                    except:
                        if(i == len(YahooMovie.Theater_DB) - 1 and ExcelRead_Name != MovieName):#判斷Excel裡是否有資料
                            print('這網頁還沒有這個電影的時刻表ㄏㄏ')
                            self.MoiveName.SetLabel("")
                            self.Taps.SetLabel("")
                            self.Theater.SetLabel("\t\t\t" + "  這網頁還沒有這個電影的時刻表ㄏㄏ")
                            self.Times.SetLabel("")
                        continue
                elif(i == len(YahooMovie.Theater_DB) - 1 and MovieName == ""):#判斷是否空白
                    print('你只會按Enter還會幹嘛?')
                    self.MoiveName.SetLabel("")
                    self.Taps.SetLabel("")
                    self.Theater.SetLabel("\t\t\t" + "            你只會按Enter還會幹嘛?")
                    self.Times.SetLabel("")
                  
class TotalApp(wx.App):
    def OnInit(self):
        self.MainForm = MainForm(None,-1)
        return True

app=TotalApp()

app.MainForm.Show()
app.MainLoop()
