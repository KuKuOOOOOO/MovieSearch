import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import xlwt
import xlrd
import os
import DateGUI
import wx

url_news = DateGUI.DateGUi.ThisWeekOrOther()                           #預設網站Yahoo電影上映中電影
#GET request from url and parse via BeautifulSoup
resp = requests.get(url_news,timeout=3)                                #跟URL要求反爬
#print(resp.text)
resp.encoding = 'utf-8'                                                 #預設編碼UTF-8
soup = BeautifulSoup(resp.text,'lxml')                                  #爬網頁code
#print(soup.text)
num_page = 1                                                            #上映中電影第一頁
times_url_links = []                                                    #時刻表URL陣列
filename = 'MovieData.xls'                                              #預設Excel檔案名稱
book = xlwt.Workbook(encoding='utf-8')                                  #創建並預設Excel編碼
sheet1 = book.add_sheet("Sheet1", cell_overwrite_ok=True)               #表格頁設置名稱Sheet1
Name_DB = []                                                              #電影名稱陣列Databsae
Date_DB = []                                                              #電影上映日期陣列Database
Theater_DB = []                                                         #電影院陣列Database
Taps_DB = []                                                            #模式陣列Database
Times_DB = []                                                           #時刻表陣列Database
def Read_Excel(row,col):
    try:
        OpenExcel = xlrd.open_workbook(filename=filename)               #Open 該Excel檔案
        Find_sheet = OpenExcel.sheet_by_name("Sheet1")                  #讀表"Sheet1"
        Find_rows = Find_sheet.row_values(row)                          #讀列
        Find_cols = Find_sheet.col_values(col)                          #讀行
        Find_form = Find_sheet.cell_value(row,col)                      #讀表格
    except Exception as e:                                              #發生任何例外狀況 回傳空白
        Find_form = ""
    return Find_form

def Excel_Output(filename,row,col,MovieArray):
    name_col = sheet1.col(0)                                            #設定名稱行
    burn_col = sheet1.col(1)                                            #設定上映日期行
    taps_col = sheet1.col(2)                                            #設定模式行
    theater_col = sheet1.col(3)                                         #設定電影院行
    times_col = sheet1.col(4)                                           #設定時刻表行
    Style = xlwt.XFStyle()                                              #隨字串長度改行寬
    first_rowW = ['電影名稱','上映時間','數位/IMAX','電影院','時刻表']  #設定第一列說明列陣列
    for i in range(0,len(first_rowW),1):                                #說明列陣列寫入第一列
        sheet1.write(0,i,first_rowW[i])
    name_col.width = 256 * 40                                           #設定名稱行初始寬度
    burn_col.width = 256 * 25                                           #設定上映日期行初始寬度
    taps_col.width = 256 * 15                                           #設定模式行初始寬度
    theater_col.width = 256 * 40                                        #設定電影院行初始寬度
    times_col.width = 256 * 100                                         #設定時刻表行初始寬度
    if(Read_Excel(row,col) == ""):                                      #如讀取表格值=空白
       sheet1.write(row,col,MovieArray)                                 #寫入電影相關事項
    book.save(filename)                                                 #儲存Excel檔案
def Times_Display(Times_URL):
    Times_url_link = []                                                 #各電影時刻表
    Times_res = requests.get(Times_URL)
    Times_res.encoding = 'utf-8'
    TimesSoup = BeautifulSoup(Times_res.text,'lxml')
    Times_gabtn = TimesSoup.find_all('a',class_='btn_s_time gabtn')     #取時刻表html
    for Times_url in Times_gabtn:                                       #將時刻表網址輸入至電影時刻表陣列
        Times_url_link.append(Times_url.get('href'))                    #取時刻表url至陣列
    return Times_url_link

def Times_DisplayTaichung():
    Times_url_link = []                                                 #各電影時刻表
    Times_urlList = list(Times_Display(url_news))                       #將時刻表轉成List
    for i in range(0,len(Times_urlList),1):                             #將List[i]拆成i個字
        Times_urlString = list(Times_urlList[i])
        Times_urlString[49] = '?'                                       #將/換成?
        Times_urlTaichung = "".join(Times_urlString) + "&area_id=2"     #將網址換成只顯示台中地區之網址
        Times_url_link.append(Times_urlTaichung)                        #將轉換後網址塞入陣列
    return Times_url_link

def Times_DisplayTheater(i):
    TimesFuture = []                                                    #未來時刻表陣列
    Times_res = requests.get(Times_DisplayTaichung()[i])
    Times_res.encoding = 'utf-8'
    TimesSoup = BeautifulSoup(Times_res.text,'lxml')
    Times_Theater = TimesSoup.find_all('li',class_='adds')              #取電影院html
    Times_Taps = TimesSoup.find_all('li',class_='taps')                 #取模式html
    Times_Times = TimesSoup.find_all('li',class_='time _c')             #取時刻表html
    regex = re.compile("\d{2}:\d{2}")                                   #正則表達式=TT:MM
    if(Times_Theater == []):                                              #判斷台中的電影院是否都沒有時刻表
        Theater_DB.append("")                                           #塞入空白
        Taps_DB.append("台中的電影院沒有撥~")                           #塞入字串並寫入Excel
        Times_DB.append("")                                             #塞入空白
        #print("台中的電影院沒有撥~")
    else:
        for Times_select in Times_Times:                                    #取時刻表內還沒上演的時間
            Times_Future = Times_select.ul('li',class_='select')            #取時刻表內還沒上演的時間
            Times_Future_Re = regex.findall(str(Times_Future))              #將html轉成時間形式TT:MM
            TimesFuture.append(Times_Future_Re)                             #TT:MM塞入未來時刻表陣列
        for i in range(0,len(Times_Theater),1):                             
            Times_TheaterString = list(Times_Theater.pop(0).stripped_strings)#電影院list輸出
            Times_TapsString = list(Times_Taps.pop(0).stripped_strings)      #模式list輸出
            Theater_DB.append(Times_TheaterString[0])                        #塞入電影院名稱
            Taps_DB.append(Times_TapsString[0])                              #塞入模式名稱
            Times_DB.append(TimesFuture[i])                                  #塞入時刻表
            #print(Times_TheaterString[0] + '\t' + Times_TapsString[0] + '\t'
                                                       #+str(TimesFuture[i]))#印出電影院+模式+時刻表
app = wx.App()
LoadingCount = 0
Load_keepGoing = True
if(Read_Excel(0,1) != ""):                                              #檢查是否已有檔案存在
   os.remove(filename)                                                  #有則刪除檔案
print('Please wait a few minute.....')
while(num_page > 0):
    resp = requests.get(url_news)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text,'lxml')
    rows_name = soup.find_all('div',class_='release_movie_name')        #取名字html
    rows_date = soup.find_all('div',class_='release_movie_time')        #取上映時間html
    progressMax = len(rows_name)
    Loading = wx.ProgressDialog("Wait", "Please wait a few minute.....", progressMax,style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE)
    for i in range(0,len(rows_name),1):                                 #取每個電影名稱、上映時間、時刻表URL
        col_name = list(rows_name.pop(0).stripped_strings)              #名字list輸出
        col_date = list(rows_date.pop(0).stripped_strings)              #上映時間list輸出
        Name_DB.append(col_name[0])
        #print(col_name[0] + '\t' + col_date[0]) #印出名字+上映時間
        print('.')
        LoadingCount = LoadingCount + 1
        wx.Sleep(0.00001)
        Load_keepGoing = Loading.Update(LoadingCount)
        for j in range(0,1,1):
            if(Read_Excel(0,1) == ""):                                  #判斷(0,1)是否為空 空則寫入(0,1) 有則寫入電影院全部後一列
                Excel_Output(filename,j + 1,0,col_name[0])              #電影名稱寫入Excel
                Excel_Output(filename,j + 1,1,col_date[0])              #上映日期寫入Excel
            else:
                Excel_Output(filename, len(Theater_DB) + 1,0,col_name[0])#電影名稱寫入Excel
                Excel_Output(filename, len(Theater_DB) + 1,1,col_date[0])#上映日期寫入Excel
        if(len(Times_Display(url_news)) > i):                            #判斷是否有時刻表
            #print('時刻表 ' + str(Times_DisplayTaichung()[i])) #印出台中時刻表URL
            Times_DisplayTheater(i)
            #print('----------------------------------------------')
        else:
            #print('還沒有時刻表~')
            #print('----------------------------------------------')
            print('.')
        for j in range(0,len(Theater_DB),1):
            Excel_Output(filename,j + 1,2,Taps_DB[j])                   #模式寫入Excel
            Excel_Output(filename,j + 1,3,Theater_DB[j])                #電影院寫入Excel
            Excel_Output(filename,j + 1,4,str(Times_DB[j]))             #時刻表寫入Excel
    num_page = num_page + 1                                             #頁碼+1
    if(num_page == 2):                                                  #判斷限制頁數(預設限制爬到第1頁)
        num_page = 0                                                    #超過則跳出迴圈
        break
    else:
        if(soup.find_all('li',class_='nexttxt disabled') == []):        #判斷是否有下一頁、有則往下、else頁碼=0
            for next_text in soup.find_all('li',class_ = 'nexttxt'):    #找li裡面的nexttxt
                for next_url in next_text.find_all('a'):                #找li裡面的a
                    url_news = next_url.get('href')                     #找a裡面的href中URL
                    times_url_links.clear()                             #時刻表URL清除
        else:
            num_page = 0
print("Success!! Please view the Excel(MovieData)!!")
