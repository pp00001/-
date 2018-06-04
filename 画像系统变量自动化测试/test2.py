# coding:utf-8
def gettab(key):
    if isinstance(key,float) or isinstance(key,int) or isinstance(key,list):
        return key
    else:
        return key.decode('utf-8')

#print(gettab('中文'))