import Stock_url as sturl
import requests
from bs4 import BeautifulSoup
import pandas as pd
data_list =[]

def Scraping():
    for url in sturl.st_ur_li: #進入url list 依次進入一個 url
        global data_list  # 這裡使用 global 的原因是要告訴 Python，我們要在函數內部修改全域變數 data_list
        user_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        result = requests.get(url,headers=user_header)
        html_text = BeautifulSoup(result.text,"html.parser")
        namediv = html_text.find_all("div", class_="D(f) Ai(c) Mb(6px)")   #找到外層的name div
        pricediv = html_text.find_all("div",class_="D(f) Jc(sb) Ai(fe)")   #找到外層的price div
        for i in namediv:
            name = i.find("h1", class_="C($c-link-text) Fw(b) Fz(24px) Mend(8px)")  #進入name div 找到股票名稱 name hi
            for q in pricediv: # 進入price div 後尋找價錢
                data = {}
                price1 = q.find("span",class_="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)")
                price2 = q.find("span",class_="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)")
                price3 = q.find("span",class_="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)")
                price4 = q.find("span")                                                                      #四種可能會出現價錢的element
                find_price_ele = True                          #debug用，用來確認是否有找到標籤
                find_name_ele = True                           #debug用，用來確認是否有找到價錢
                if name == None:                               #製作尋找Stock_name條件
                    print("沒有找到股票名稱tag及股票名稱")
                else:
                    if name.getText() != None:
                        stock_name=name.getText()              #順利找到即放入stock_name 變數中
                        if price1 == None:
                            find_price_ele = False
                        else:
                            if price1.getText() != None:
                                price_value = price1.getText()
                                find_price_ele = True
                                data["股票名稱"] = stock_name
                                data["價格"] = price_value
                                data_list.append(data)
                                # print(f"股票名稱{stock_name},價格:{price_value},price1:{find_price_ele}")
                                break 
                            else:
                                find_price_ele =False
                                print(f"price1沒有找到{stock_name}股票價格")
                        if price2 == None:
                            find_price_ele = False
                        else:
                            if price2.getText() != None:
                                price_value = price2.getText()
                                find_price_ele = True
                                data["股票名稱"] = stock_name
                                data["價格"] = price_value
                                data_list.append(data)
                                # print(f"股票名稱{stock_name},價格:{price_value},price2:{find_price_ele}")
                                break 
                            else:
                                find_price_ele =False
                                print(f"price2沒有找到{stock_name}股票價格")
                        if price3 == None:
                            find_price_ele = False
                        else:
                            if price3.getText() != None:
                                price_value = price3.getText()
                                find_price_ele = True
                                data["股票名稱"] = stock_name
                                data["價格"] = price_value
                                data_list.append(data)
                                # print(f"股票名稱{stock_name},價格:{price_value},price3:{find_price_ele}")
                                break 
                            else:
                                find_price_ele =False
                                print(f"price3沒有找到{stock_name}股票價格")
                        if price4 == None:
                            find_price_ele = False
                        else:
                            if price4.getText() != None:
                                price_value = price4.getText()
                                find_price_ele = True
                                data["股票名稱"] = stock_name
                                data["價格"] = price_value
                                data_list.append(data)
                                # print(f"股票名稱{stock_name},價格:{price_value},price4:{find_price_ele}")
                                break 
                            else:
                                find_price_ele =False
                                print(f"price4沒有找到{stock_name}股票價格")
                    else:
                        find_name_ele = False
                        print("沒有找到股票名稱")


                        
if __name__ =="__main__":
    Scraping()
    st = pd.DataFrame(data_list)
    st.to_excel("stock_data.xlsx",index=False,engine="openpyxl")
            
# if __name__ =="__main__":
#     try:
#         Scraping()
#         print(data_list)
#     except:
#         print("Somethoing Error")



#<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">36.28</span>
#<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)">50.1</span>
#<div class="D(f) Ai(fe) Mb(4px)"><span class="Fz(32px) Fw(b) Lh(1) Mend(4px) D(f) Ai(c) C($c-trend-up)">186.19</span><span class="Mend(16px) C(#232a31) Fz(20px) Fw(600) Lh(28px)">USD</span><span class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"><span class="Mend(4px) Bds(s)" style="border-color:transparent transparent #ff333a transparent;border-width:0 6.5px 9px 6.5px"></span>1.05</span><span class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)">(0.57%)</span></div>