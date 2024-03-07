import Scraping_Stock_All as sp

sp.Scraping()

for i in sp.data_list:
    try:
        name = i["股票名稱"]
        pr1 = i["價格"]
        pr2 = pr1.replace(",","")
        price = float(pr2)
    except:
        print(f"{name}爬取到的資訊有誤")
    try:
        print(f"{name} {price}")
    except:
        print("Print error.")

    try:
        if name == "元大高股息" and price >= 36:
            print(f"{name}可考慮賣出，已達高價36")
        elif name == "元大高股息" and price <= 34.13:
            print(f"{name}可考慮止血，目前已跌小於34.13")
    except:
        print(f"{name} comparison error.")

    try:
        if name == "國泰永續高股息" and price >= 21.6:
            print(f"{name}可考慮賣出，已達高價21.6")
        elif name == "國泰永續高股息" and price <= 21.12:
            print(f"{name}可考慮止血，目前已跌小於21.12")
    except:
        print(f"{name} comparison error.")

    try:
        if name == "聯發科" and price >= 952:
            print(f"{name}可考慮賣出，目前已達高價952")
        elif name == "聯發科" and price <= 924:
            print(f"{name}可考慮止血，目前已跌小於924")
    except:
        print(f"{name} comparison error.")

    try:
        if name == "中鴻" and price >= 33:
            print(f"{name}可考慮賣出，目前已達第一個目標價33")
        elif name == "中鴻" and price >= 41:
            print(f"{name}可考慮賣出，目前已達第二個目標價41")
        elif name == "中鴻" and price >= 46:
            print(f"{name}可考慮賣出，目前已達最後一個目標價46")
        elif name == "中鴻" and price <= 22.8:
            print(f"{name}又開跌可觀察一下，目前已跌小於22.8")
    except:
        print(f"{name} comparison error.")

    try:
        if name == "聯電" and price >= 56.5:
            print(f"{name}可考慮賣出一點，目前已答第一個目標價56.5")
        elif name == "聯電" and price >= 60:
            print(f"{name}可考慮賣出一點，目前已答第二個目標價60")
        elif name == "聯電" and price <= 48.4:
            print(f"{name}又再次開跌，目前已跌小於48.4")
    except:
        print(f"{name} comparison error.")

    try:
        if name == "鴻海" and price >= 111:
            print(f"{name}可考慮賣出一點，目前已答第一個目標價111")
        elif name == "鴻海" and price >= 116:
            print(f"{name}可考慮賣出一點，目前已答第二個目標價116")
        elif name == "鴻海" and price <= 96.5:
            print(f"{name}又再次開跌，目前已跌小於48.4")
    except:
        print(f"{name} comparison error.")
    try:    
        if name == "華邦電" and price >= 31.7:
            print(f"{name}可考慮賣出，目前已答第一個目標價31.7")
        elif name == "華邦電" and price <= 27.35:
            print(f"{name}又再次開跌，目前已跌小於27.35")
    except:
        print(f"{name} comparison error.")
    try:
        if name == "陽明" and price >= 72:
            print(f"{name}可考慮賣出一點，目前已答第一個目標價72")
        elif name == "陽明" and price >= 94:
            print(f"{name}可考慮賣出一點，目前已答第二個目標價60")
        elif name == "陽明" and price >= 110:
            print(f"{name}可考慮賣出一點，目前已答第三個目標價60")
        elif name == "陽明" and price >= 125:
            print(f"{name}可考慮賣出一點，目前已答第四個目標價60")
        elif name == "陽明" and price <= 46.5:
            print(f"{name}又再次開跌，目前已跌小於46.5")
    except:
        print(f"{name} comparison error.")
    try:
        if name == "華航" and price >= 24.3:
            print(f"{name}可考慮賣出，目前答第一目標價24.3")
        elif name == "華航" and price <= 20.7:
            print(f"{name}可考慮止血，目前已跌小於20.7")
    except:
        print(f"{name} comparison error.")
    try:
        if name == "群創" and price >= 17:
            print(f"{name}可考慮賣出一點，目前已答第一個目標價17")
        elif name == "群創" and price >= 20:
            print(f"{name}可考慮賣出一點，目前已答第二個目標價20")
        elif name == "群創" and price <= 14.1:
            print(f"{name}又再次開跌，目前已跌小於14.1")
    except:
        print(f"{name} comparison error.")


    

