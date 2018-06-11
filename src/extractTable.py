from tabula import convert_into
import re
from TableExtractFunction import isKeywordInTable, printVal
from convertPDFToImage import val
from nesFun import isKeyWord, readKeyWord




def tableExtract(path, GST):
    listy = []
    order = []
    data = []
    keyList = []
    t = val(path)
    convert_into(t, "output.tsv", output_format="tsv")
    cnt = open("output.tsv", "r")
    txt = cnt.read()
    listy = txt.split("\n")
    i = 0
    for i in range(0, len(listy)):
        listy[i] = re.split("\t| ", listy[i])

    i = 0
    # for l in listy:
    #     print(l)
    if isKeywordInTable(listy[2]):
        try:
            while i < len(listy[0]) and i < len(listy[2]):
                tmp = listy[0][i] + listy[2][i]
                if tmp:
                    order.append(tmp)
                if listy[1][i] and i < len(listy[i]):
                    while listy[1][i]:
                        order.append(listy[1][i])
                        i += 1
                i += 1
        except:
            print(i)
        i = 3
    else:
        order = listy[0]
    orderHeading(order)
    print(order)
    h = ''
    keyList = readKeyWord()
    while i < len(listy):
        j = 0
        try:
            int(listy[i][0])
            j += 1
        except:
            print('')
        flag = False
        while j < len(listy[i]):
            if listy[i][j]:
                try:
                    tmp = float(str(listy[i][j]).replace(',', '').replace('?', "").replace('%', ''))
                    falg = True
                    if h:
                        if isKeyWord(keyList, h):
                            data.append(h)
                        else:
                            printVal(GST, data)
                            data.clear()
                            data.append(h)
                        h = ''
                        flag = True
                    data.append(tmp)
                except:
                    h += listy[i][j]
            j += 1
        i += 1
