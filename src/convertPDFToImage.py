from PIL import Image
import os

fileName = 'Invoiceimg.jpg'


def val(path):
    im = Image.open(path)
    if im.mode == 'RGBA':
        im = im.convert('TGB')
    if os.path.exists(path.split(".")[0]+".pdf"):
        im.save(path.split(".")[0]+"s.pdf", "PDF", resolution=300.0)
        return path.split(".")[0]+".pdf"


if __name__ == '__main__':
    val(fileName);
