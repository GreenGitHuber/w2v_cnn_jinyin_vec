import pandas as pd 
import numpy as np
import os
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

PATH = os.getcwd()
#/Users/jiangqy/Code/preprocess_for_cnn/bin
model = Word2Vec.load('./model/wiki.zh.text.model')
def read_file(path):
	file_list=[]
	with open(path,'r') as f:
		for line in f.readlines():
			line=line.strip()
			word_list=line.split(" ")
			file_list.append(word_list)
	return file_list

#对于不存在的词汇用一些0向量来替换
def unkown_vec(size):
	unkown_vec = embeddingUnknown = [0 for i in range(size)]
	return unkown_vec

#将拼音转化为向量
#并且对于预处理当中没有过滤的字母进行随机
def py_vec(string):
	vec = [0]*26
	for char in string:
		if char.isalpha():
			loc = ord(char)- ord('a')
			if loc not in range(0,26):
				vec = [0 for i in range(26)]
				return vec
			vec[loc] = 1
	return vec

#将处理好的文本变为词向量
#这一步的关键是有时候训练好的模型没有分类文本的词
#所以采用随机赋值一个向量给这个词
def article_vec(word):
	try:
		vc = model.wv[word]
	except Exception as e:		
		vc = unkown_vec(400)
	return vc
	

# if __name__=='__main__':
# 	print ("ok")
# 	#path_cn='../corpus/zhaospam_af_jieba.txt'
# 	#path_py='../corpus/zhaospam_to_pinyin.txt'
# 	path_cn='../corpus/zh_test.txt'
# 	path_py='../corpus/zhpinyin_test.txt'
# 	res_cn=read_file(path_cn)
# 	res_py=read_file(path_py)
# 	res_vec = []
# 	for a,b in zip(res_cn,res_py):
# 		this_vec = []
# 		for item_a,item_b in zip(a,b):
# 			vec1_arr=article_vec(item_a)
# 			vec2=py_vec(item_b)
# 			vec2_arr=np.array(vec2)
# 			this_vec.append(np.concatenate((vec1_arr,vec2_arr)))
# 			this_vec_arr=np.array(this_vec)
# 		res_vec.append(this_vec_arr)

# 	x = np.array(res_vec)

# def embedding_sentences(positive_path_cn,positive_path_py,negative_path_cn,negative_path_py):
# 	res_cn=read_file(positive_path_cn)
# 	res_py=read_file(positive_path_py)
# 	res_vec = []
# 	for a,b in zip(res_cn,res_py):
# 		this_vec = []
# 		for item_a,item_b in zip(a,b):
# 			vec1_arr=article_vec(item_a)
# 			vec2=py_vec(item_b)
# 			vec2_arr=np.array(vec2)
# 			this_vec.append(np.concatenate((vec1_arr,vec2_arr)))
# 			this_vec_arr=np.array(this_vec)
# 		res_vec.append(this_vec_arr)
# 	return res_vec



	


	
