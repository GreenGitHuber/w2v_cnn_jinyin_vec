# -*- coding: utf-8 -*-

'''
python word2vec_helpers.py input_file output_model_file output_vector_file
'''

# import modules & set up logging
import os
import sys
import logging
import multiprocessing
import time
import json
import data_helpers
import numpy as np
 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def output_vocab(vocab):
    for k, v in vocab.items():
        print(k)


def embedding_sentences(sentences, embedding_size = 128, window = 5, min_count = 5, file_to_load = None, file_to_save = None):
    if file_to_load is not None:
        w2vModel = Word2Vec.load(file_to_load)
    else:
        w2vModel = Word2Vec(sentences, size = embedding_size, window = window, min_count = min_count, workers = multiprocessing.cpu_count())
        if file_to_save is not None:
            w2vModel.save(file_to_save)
    all_vectors = []
    embeddingDim = w2vModel.vector_size
    print("vector size:", embeddingDim)

    embeddingUnknown = [0 for i in range(embeddingDim)]
    #原代码
    # for sentence in sentences:
    #     this_vector = []
    #     for word in sentence:
    #         if word in w2vModel.wv.vocab:
    #             this_vector.append(w2vModel[word])
    #         else:
    #             this_vector.append(embeddingUnknown)
    #     all_vectors.append(this_vector)
    # return all_vectors
#+++++++++++++++++++++++++++++++++++++++++++++++++
#加拼音向量
    test_times=0
    for sentence in sentences:
        
        print (test_times ,'   ',len(sentences))
        test_times=test_times+1

        this_vector = []
        for word in sentence:
            if word in w2vModel.wv.vocab:
                #print (word)
                zh_vec = w2vModel[word]
                py_vec = data_helpers.word_to_vec(word)
                merge_vec = np.concatenate((zh_vec,py_vec))
                this_vector.append(merge_vec)
            else:
                #print (word)
                zh_vec = embeddingUnknown
                py_vec = data_helpers.word_to_vec(word)
                merge_vec = np.concatenate((zh_vec,py_vec))
                this_vector.append(merge_vec)               
        all_vectors.append(this_vector)
    print("over!!!!!")
    return all_vectors


#++++++++++++++++++++++++++++++++++++++++++++++++++

def generate_word2vec_files(input_file, output_model_file, output_vector_file, size = 128, window = 5, min_count = 5):
    start_time = time.time()

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model = Word2Vec(LineSentence(input_file), size = size, window = window, min_count = min_count, workers = multiprocessing.cpu_count())
    model.save(output_model_file)
    model.wv.save_word2vec_format(output_vector_file, binary=False)

    end_time = time.time()
    print("used time : %d s" % (end_time - start_time))

def run_main():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
    if len(sys.argv) < 4:
        print (globals()['__doc__'] % locals())
        sys.exit(1)
    input_file, output_model_file, output_vector_file = sys.argv[1:4]

    generate_word2vec_files(input_file, output_model_file, output_vector_file) 

def test():
    vectors = embedding_sentences([['first', 'sentence'], ['second', 'sentence']], embedding_size = 4, min_count = 1)
    print(vectors)
