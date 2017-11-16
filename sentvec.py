import gensim
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from numpy import dot
from numpy.linalg import norm
model = gensim.models.KeyedVectors.load_word2vec_format('/home/aditi/Desktop/nlp/glove_vec.text');
example_sent = "give me the list of assets related to machine learning"
sent_two = "what assets do you have under machine learning"

text_file = open("stopwords.txt", "r")
lines = text_file.readlines()

stop_words =[]
for i in lines:
    stop_words.append(i.replace('\n',''))


#stop_words = set(stopwords.words('english'))        
word_tokens1 = word_tokenize(example_sent)
filtered_sentence1 = []
for w in word_tokens1:
    if w not in stop_words:
        filtered_sentence1.append(w)
print filtered_sentence1

word_tokens2 = word_tokenize(sent_two)  
filtered_sentence2 = []
for w in word_tokens2:
    if w not in stop_words:
        filtered_sentence2.append(w)
print filtered_sentence2



sentvec1 = np.zeros(50)
for w in filtered_sentence1:
    if w in model.vocab:
        sentvec1 = (sentvec1 + model[w])
sentvec1 = sentvec1/len(sentvec1) 
#print sentvec1

sentvec2 = np.zeros(50)
for w in filtered_sentence2:
    if w in model.vocab:
        sentvec2 = (sentvec2 + model[w])/2
sentvec2 = sentvec2/len(sentvec2)   
#print sentvec2

cos_sim = dot(sentvec1, sentvec2)/(norm(sentvec1)*norm(sentvec2))
print cos_sim