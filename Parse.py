strDate = ""
strSen = ""
strLine = ""
strSum = ""
#strFirst = ""
strCheck = ""
iGo = 1

f2 = open('output.txt','w+')
f = open('line.txt')


for i in range(1, 65000, 1):
    #讀取一行資料
    strLine = f.readline()
    #讀取前面四個字看是不是日期的那行
    strCheck = strLine[:4]
    if strCheck.isdigit():
        strDate = strLine
        #-----------------
        if strSum != "":
            f2.write(strSum)
            #print("write: " + strSum)
            strSum = ""
        #-----------------
    #如果第三個字元是":"，代表是對話行
    if len(strLine) > 2 :
        strSen = strLine[2]
        if strSen == ':':
            #strSum 有值，代表有處理過
            #-----------------
            if strSum != "":
                f2.write(strSum)
                #print("write: " + strSum)
                strSum = ""
            #-----------------
            strDate = strDate.replace(chr(10),chr(9))
            strSum = strDate + strLine
            #print("in: " + strSum)
    #-----------------
#    if (strCheck.isdigit() and (strSen != ':')):
#    if (strSum != ""):
#        f2.write((strSum + strLine).replace(chr(10),chr(9),1))
#        strSum = ""
    #-----------------
    #print("strSen: " + strSen + " strSum: " + strSum + " strLine: " + strLine + " strDate: " + strDate)

f.close()
f2.close()
print("down")












"""
while iGo:
    #讀取一行資料
    strLine = f.readline()

    #讀取前面四個字看是不是日期的那行
    strCheck = strLine[:4]
    if strCheck.isdigit():
        strDate = strLine
        while iTemp:
            strLine = f.readline()
            if strSum != "":
                f2.write(strSum)
                strSum = ""

            #如果第三個字元是":"，代表是對話行
            if len(strLine) > 2 :
                strSen = strLine[2]
                if strSen == ':':
                    strDate = strDate.replace(chr(10),chr(9))
                    strSum = strDate + strLine

            #如果不是日期也不是時間開頭的話，就是上一行的對話分行
            IF ord(strLine[0]) > 256:
                strSum = strSum.replace(chr(10),chr(32),1) + strLine



for i in range(1, 501, 1):
    #讀取一行資料
    strLine = f.readline()
    #讀取前面四個字看是不是日期的那行
    strCheck = strLine[:4]
    if len(strLine) > 2 :
        strSen = strLine[2]
    #讀取當天的對話紀錄做重新組合
    #print("last ch: " + str(ord(sum[-1:])))
    #如果前面四個字是數字，代表是日期那行
    if strCheck.isdigit():
        strDate = strLine
    #如果第三個字元是":"，代表是對話行
    if strSen == ':':
        strDate = strDate.replace(chr(10),chr(9))
        strSum = strDate + strLine
        f2.write(strSum)
    else :
        #不是日期也不是對話，就是有chr(10)的上一個句子，直接加
        strSum = strLine.replace(chr(10),chr(32))
        f2.write(strSum + chr(10))
"""


"""
for line in f:
    print(line)
f.close()


for i in range(1, 101, 1):
    sum += i
print(sum)

"""
