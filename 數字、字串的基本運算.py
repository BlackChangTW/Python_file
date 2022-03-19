###數字運算
print(6 + 3) #加法
print(6 - 3) #減法5
print(6 * 3) #乘法
print(6 / 3) #除法
print(6 // 3) #整數除法(不除到小數位)
print(2 ** 3) #次方計算
print(7 % 3) #取餘數

x = 2 + 3
print(x)
x = x + 1 #將變數中的數字+1
print(x)

###字串運算
print('Hello World') #單引號
print("Hello World") #雙引號
print('Hell\"o World') #使用\" 在字串中顯示雙引號
print("Hello" + " World") #使用+ 讓兩個不同的字串串接成同個字串
print("Hello" " World") #在兩個字串中加入空格 讓兩個不同的字串串接成同個字串
print("Hello\nWorld") #在字串中使用\n換行
print("""Hello
World""") #在括號外面加上三個雙因號貨單引號即可直接換行
print("Hello " * 3) #在字串外面加上乘號 數字 即可重複字串

#字串會對內部的資字元編號(索引) 從0開始算起 
print("Hello World"[0]) #0代表"Hello World"中的第一個字元"H"
print("Hello World"[2]) #2代表"Hello World"中的第三個字元"l"
print("Hello World"[1:4]) #取得索引字元1~4 包含開頭 不包含結尾
print("Hello World"[1:]) #取得索引字元1~ 從開頭到結尾
print("Hello World"[:4]) #取得所引字元~4 結尾前所有字 不包括結尾