import sqlite3

import pandas
#from sklearn.naive_bayes import GaussianNB as nb

last = {'SNO', 'Desc', 'Quantity', 'Amount'}
last1 = {'Desc', 'Quantity', 'Amount', 'taxamount'}
df = pandas.read_csv("tabfields.csv")


def isKeywordInTable(val=[]):
    for t in val:
        for i in last:
            for v in df[i]:
                if str(t).lower() == str(v).lower():
                    return True
    return False


def gst(args):
    pass


def printVal(GST, val=[]):
    if val:
        n = len(val)
        i = 0
        # print(GST)
        for v in val:
            if i == 0:
                # print(v)
                des = str(v)
            if i == n - 1:
                # print(v)
                amt = str(v)
            if i == 3:
                # print(v)
                qan = str(v)
            i += 1
        # print(des + " " + qan + " " + amt)
        push(GST, des, qan, amt)


# def orderHeading(val=[]):
#     model = nb()
#     for v in val:
#         try:
#             train = df[v] < 0.7
#             test = df[v] < 0.3
#             if model.fit(train, test) > 0:
#                 return True
#             else:
#                 return False
#         except:
#             print()


def push(gst, des, qan, amt):
    print(gst + " " + des + " " + qan + " " + amt)
    conn = sqlite3.connect('InvoiceDB.db')
    c = conn.cursor()
    c.execute('INSERT INTO TableInv VALUES(?,?,?,?)', (gst, des, qan, amt))
    # m=m+1\
    conn.commit()
