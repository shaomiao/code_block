import os

# import time
import time


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath + "\\", allDir))
        f = open(child,)
        MyRomStr = f.read()
        f.close()
        str = time.strftime('%Y-%m-%d', time.localtime(time.time())).encode('utf-8')
        MyFileStr =   str.decode("gb2312")
        f = open(child,"wb")
        f.write((MyFileStr+MyRomStr).encode("utf-8"))
        print(child + "已经写入")
        f.close()


filepaht = "D:\ceshi"
eachFile(filepaht)
