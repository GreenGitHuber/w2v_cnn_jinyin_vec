# -*- coding:utf-8 -*-
# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from pinyin import PinYin

def sentences_to_pinyin(file_path,file_to_save_path):
    test = PinYin()
    test.load_word()
    raw = open(file_path)
    line = raw.readline()
    py_str = ''
    while line:
        string = test.hanzi2pinyin_split(string=line,split="")
        py_str += string
        line = raw.readline()
    raw.close()
    with open(file_to_save_path,'w') as f:
        f.write(py_str)

def word_to_pinyin(word):
    test = PinYin()
    test.load_word()
    word_py = test.hanzi2pinyin_split(string=line,split="")
    return word_py


# if __name__ == "__main__":
#     test = PinYin()
#     test.load_word()
#     raw = open(r"../corpus/zh_test.txt")
#     line = raw.readline()
#     str = ''
#     while line:
#         string = test.hanzi2pinyin_split(string=line,split="")
#         str += string
#         line = raw.readline()
#     raw.close()
#     f=open("../corpus/zhpinyin_test.txt",'wb')
#     f.write(str)
#     f.close()
    
    # pinyin_str = test.hanzi2pinyin_split(string=string, split=" ")
    # joint_str = string pinyin_str
    # print "out: %s" % str(test.hanzi2pinyin(string=string))
    # print "out: %s" % test.hanzi2pinyin_split(string=string, split="-")
    # print joint_str
    # print string
