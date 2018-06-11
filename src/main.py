import pytesseract
import re
from PIL import Image

from extractTable import tableExtract
from nesFun import isKeyWord, push, isEmpty, isPincode, printList, rearrageList, insertIntoDB

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

def mainFun(path):
    im = Image.open(path)
    keyWords = []
    companyNames = []
    # reading the keywords
    with open('keyword.txt', 'r') as fp:
        keyWords = (fp.readlines())
    # readling company names
    text = pytesseract.image_to_string(im, lang='eng')
    lines = []
    for s in text.split("\n"):
        if s:
            lines.append(s)

    print("The list has been updated")
    i = 0
    print(lines)
    while i < len(lines):

        word = re.split(":|-|~|#", lines[i])
        # print(word)
        # lines[i].split(":")

        if isKeyWord(keyWords, word[0]):

            if (isEmpty(word[1])):
                i += 1

                while (i < len(lines)):

                    flag = False
                    word[1] += " " + lines[i]
                    str = lines[i].split(", ")

                    for fu in str:

                        if (isPincode(fu)):
                            flag = True
                            break

                    if flag:
                        break

                    i += 1
            push(word)
        i += 1
    lines = rearrageList()
    i = 0
    for s in lines:
        if i == 0:
          gst = s
        print(s)
        i += 1
    #print(gst)
    insertIntoDB(lines)
    tableExtract(path, gst)
