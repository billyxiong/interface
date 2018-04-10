# --*-- coding = utf-8 --*--
import re
with open('C:\\Users\\Administrator\\Desktop\\apis.js','r') as f:
    print re.findall(r"url: '(.+?)',",f.read().decode('utf-8'))