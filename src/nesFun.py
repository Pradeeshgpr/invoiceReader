import sqlite3

import pandas
import re
list = []
orderedList = ["1", "2", "3", "4", "5", "6", "7"]
index = pandas.read_csv("fields.csv")
keyWordList = ["gst", "invoice id", "Order", "PAN NO", "Retailer", "Shipping info", "Delivered to"]


def isKeyWord(wordList, word):
    for s in wordList:
        if str(s).lower().strip("\n").strip(" ") == str(word).lower():
            return True
    return False

def readKeyWord():
    with open('keyword.txt', 'r') as fp:
        keyWords = (fp.readlines())
    return keyWords

def push(word):
    list.append(word)


def isEmpty(word):
    if not word:
        return True
    return False

def isPincode(pinCde):
    txt = re.split(":|—", pinCde)
    for pinCode in txt:
    # if len(pinCode) < 6:
    #     return False
    # if len(pinCode) > 6:
    #     return False
        if str(pinCode).isdigit():
            if 6 == len(pinCode):
                return True
    return False


def printList():
    for s in orderedList:
        print(s)


def getIndex(strings):
    j = 0
    for i in keyWordList:
        for s in index[i]:
            if str(s).lower() == str(strings).lower():
                return j
        j += 1
    return -1


def rearrageList():
    for i in list:
        tmp = i[0]
        orderedList[getIndex(tmp)] = i[1]
    # printList()
    return orderedList

def insertIntoDB(keyList):

    conn = sqlite3.connect('InvoiceDB.db')
    c = conn.cursor()

    c.execute('INSERT INTO InvoiceDB(GST,Invoice,PAN,Orders,Retailer,Shipped,Delivered) VALUES(?,?,?,?,?,?,?)', (keyList[0], keyList[1], keyList[2], keyList[3], keyList[4], keyList[5], keyList[6]))
        #m=m+1\
    conn.commit()
