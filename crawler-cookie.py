# 抓取 PTT 電影版的網頁原始碼（HTML)
import urllib.request as req 

def getData(url):
   # 建立一個 Request物件，附加 Request Headers 的資訊
   request=req.Request(url, headers={
      "cookie":"over18=1",
      "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
   })
   with req.urlopen(request) as response:
      data = response.read().decode("utf-8")

   # 解析原始碼，取得每篇文章的標題
   import bs4 
   root = bs4.BeautifulSoup(data, "html.parser")
   titles = root.find_all("div", class_="title") # 尋找class ＝ "title" 的 div 標籤
   for title in titles:
      if title.a != None: #如果標題含 a 標籤（沒有被刪除），印出標題
         print(title.a.string)

   # 抓取上一頁的連結
   nextLink = root.find("a", string="‹ 上頁") # 找到內文是 < 上頁 的 a 標籤
   return nextLink["href"]

#抓取一個頁面的標題
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count<3:
   pageURL = "https://www.ptt.cc" + getData(pageURL)
   count+=1 
