import Scraping_Stock_All as sp

sp.Scraping()

for i in sp.data_list:
    try:
        name = i["股票名稱"]
        pr = i["價格"]
        price = float(pr)
        try:
            if name == "元大高股息":
                print(f"{name}目前價格{price},目標36,低於34.13止血")
            if name == "元大高股息" and price >= 36:
                print(f"{name}可考慮賣出，已達36")
            elif name == "元大高股息" and price <= 34.13:
                print(f"{name}可考慮止血，目前價格已跌低於34.13")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "國泰永續高股息":
                print(f"{name}目前價格{price},目標21.6,低於21.12止血")            
            if name == "國泰永續高股息" and price >= 21.6:
                print(f"{name}可考慮賣出，已達21.6")
            elif name == "國泰永續高股息" and price <= 21.12:
                print(f"{name}可考慮止血，目前價格已跌低於21.12")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "聯發科":
                print(f"{name}目前價格{price},目標980,低於924止血")    
            if name == "聯發科" and price >= 980:
                print(f"{name}可考慮賣出，目前已達980")
            elif name == "聯發科" and price <= 924:
                print(f"{name}可考慮止血，目前價格已跌低於924")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "中鴻":
                print(f"{name}目前價格{price},目標價格33 41 46 ,低於22.8止血")               
            if name == "中鴻" and price >= 33:
                print(f"{name}可考慮賣出，目前已達第一個目標價33")
            elif name == "中鴻" and price >= 41:
                print(f"{name}可考慮賣出，目前已達第二個目標價41")
            elif name == "中鴻" and price >= 46:
                print(f"{name}可考慮賣出，目前已達最後一個目標價46")
            elif name == "中鴻" and price <= 22.8:
                print(f"{name}可考慮止血，目前價格已跌低於22.8")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "聯電":
                print(f"{name}目前價格{price},目標56.5 60,低於48.4止血")    
            if name == "聯電" and price >= 56.5:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價56.5")
            elif name == "聯電" and price >= 60:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價60")
            elif name == "聯電" and price <= 48.4:
                print(f"{name}可考慮止血，目前價格已跌低於48.4")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "鴻海":
                print(f"{name}目前價格{price},目標111 116,低於96.5止血")  
            if name == "鴻海" and price >= 111:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價111")
            elif name == "鴻海" and price >= 116:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價116")
            elif name == "鴻海" and price <= 96.5:
                print(f"{name}可考慮止血，目前價格已跌低於96.5")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "華邦電":
                print(f"{name}目前價格{price},目標31.7,低於27.35止血")      
            if name == "華邦電" and price >= 31.7:
                print(f"{name}可考慮賣出，目前已答第一個目標價31.7")
            elif name == "華邦電" and price <= 27.35:
                print(f"{name}可考慮止血，目前價格已跌低於27.35")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "陽明":
                print(f"{name}目前價格{price},目標72 60 110 125,低於46.5止血")   
            if name == "陽明" and price >= 72:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價72")
            elif name == "陽明" and price >= 94:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價60")
            elif name == "陽明" and price >= 110:
                print(f"{name}可考慮賣出一點，目前已答第三個目標價110")
            elif name == "陽明" and price >= 125:
                print(f"{name}可考慮賣出一點，目前已答第四個目標價125")
            elif name == "陽明" and price <= 46.5:
                print(f"{name}可考慮止血，目前價格已跌低於46.5")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "華航":
                print(f"{name}目前價格{price},目標24,3,低於20.7止血")   
            if name == "華航" and price >= 24.3:
                print(f"{name}可考慮賣出，目前答第一目標價24.3")
            elif name == "華航" and price <= 20.7:
                print(f"{name}可考慮止血，目前價格已跌低於20.7")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "群創":
                print(f"{name}目前價格{price},目標 17 20,低於14.1止血")               
            if name == "群創" and price >= 17:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價17")
            elif name == "群創" and price >= 20:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價20")
            elif name == "群創" and price <= 14.1:
                print(f"{name}可考慮止血，目前價格已跌低於14.1")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "廣豐":
                print(f"{name}目前價格{price},目標13.05 20,低於11.65止血")               
            if name == "廣豐" and price >= 13.05:
                print(f"{name}目前已答第一個目標價13.05")
            elif name == "廣豐" and price >= 20:
                print(f"{name}目前已答第二個目標價20")
            elif name == "廣豐" and price <= 11.65:
                print(f"{name}可考慮止血，目前價格已跌低於11.65")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "中鋼":
                print(f"{name}目前價格{price},目標30 33,低於25止血")               
            if name == "中鋼" and price >= 30:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價30")
            elif name == "中鋼" and price >= 33:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價33")
            elif name == "中鋼" and price <= 25:
                print(f"{name}可考慮止血，目前價格已跌低於25")
        except:
            print(f"{name} occur something error.")             

        try:
            if name == "旺宏":
                print(f"{name}目前價格{price},目標33.8 39.3,低於28.5止血")               
            if name == "旺宏" and price >= 33.8:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價33.8")
            elif name == "旺宏" and price >= 39.3:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價39.3")
            elif name == "旺宏" and price <= 28.5:
                print(f"{name}可考慮止血，目前價格已跌低於28.5")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "茂矽":
                print(f"{name}目前價格{price},目標38 43.25,低於31.5止血 ")               
            if name == "茂矽" and price >= 38:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價38")
            elif name == "茂矽" and price >= 43.25:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價43.25")
            elif name == "茂矽" and price <= 31.5:
                print(f"{name}可考慮止血，目前價格已跌低於31.5")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "宏碁":
                print(f"{name}目前價格{price},目標45 55 66,低於44止血")               
            if name == "宏碁" and price >= 45:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價45")
            elif name == "宏碁" and price >= 55:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價55")
            elif name == "宏碁" and price >= 66:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價66")
            elif name == "宏碁" and price <= 44:
                print(f"{name}漲了又跌，目前價格已跌低於44")
        except:
            print(f"{name} occur something error.") 

        try:
            if name == "友達":
                print(f"{name}目前價格{price},目標20.55 23,低於17.4止血")               
            if name == "友達" and price >= 20.55:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價20.55")
            elif name == "友達" and price >= 23:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價23")
            elif name == "友達" and price <= 17.4:
                print(f"{name}可考慮止血，目前價格已跌低於17.4")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "遠百":
                print(f"{name}目前價格{price},目標24 25.05,低於23.99止血")               
            if name == "遠百" and price >=24:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價24")
            elif name == "遠百" and price >= 25.05:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價25.05")
            elif name == "遠百" and price <= 23.99:
                print(f"{name}可考慮止血，目前價格已跌低於23.99")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "懷特":
                print(f"{name}目前價格{price},目標23.4 26,低於21.5止血")               
            if name == "懷特" and price >= 23.4:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價23.4")
            elif name == "懷特" and price >= 26:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價26")
            elif name == "懷特" and price <= 21.5:
                print(f"{name}可考慮止血，目前價格已跌低於21.5")
        except:
            print(f"{name} occur something error.")

        try:
            if name == "力積電":
                print(f"{name}目前價格{price},目標28.9 31,低於26.75止血")               
            if name == "力積電" and price >= 28.9:
                print(f"{name}可考慮賣出一點，目前已答第一個目標價28.9")
            elif name == "力積電" and price >= 31:
                print(f"{name}可考慮賣出一點，目前已答第二個目標價31")
            elif name == "力積電" and price <= 26.75:
                print(f"{name}可考慮止血，目前價格已跌低於26.75")
        except:
            print(f"{name} occur something error.")                     
    except:
        print(f"{name}爬取到的{pr}，無法進入判斷式")
        

    

