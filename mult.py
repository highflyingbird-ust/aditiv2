import nltk
import gensim
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format('/home/aditi/Desktop/nlp/glove_vec.text');

input = raw_input('Type here: ')
tok = nltk.word_tokenize(input.lower());

vec = []
for i in tok:
    vec.append(model[i])

mat = []
for i in tok:
    mat.append(np.identity(50)+np.random.randn(50,50))

pair = []
for i in range(len(tok)):
    pair.append([vec[i],mat[i]])

