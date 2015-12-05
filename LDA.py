from os import listdir, chdir
import sys
import string
import textmining
import numpy as np
import lda
from nltk.stem.porter import *
from scipy import spatial

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

OUTPUT_DIR = "/media/mitesh/Personal/Projects/Enron Email Graph Generation/graph_mining/Pre-Processed"
chdir(OUTPUT_DIR)

tdm = textmining.TermDocumentMatrix()
names = [d for d in listdir(".") if "." in d]
print names


stemmer = PorterStemmer()
for name in names:
    sentence_list=""
    word_list = []
    for line in open(OUTPUT_DIR+"/%s"% (name), 'r').readlines():    
        sentence_list = sentence_list + line
    tdm.add_doc(sentence_list)
temp = list(tdm.rows(cutoff=1))
vocab = tuple(temp[0])
print vocab
X = np.array(temp[1:])

model = lda.LDA(n_topics = 10, n_iter = 200, random_state = 1)
model.fit(X)
topic_word = model.topic_word_

#printing some more info
#print("type(topic_word): {}".format(type(topic_word)))
#print("shape: {}".format(topic_word.shape))

n = 10
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

doc_topic = model.doc_topic_

for i in range(len(names)):
    for j in range(len(names)):
        if i != j:
            dist =spatial.distance.cosine(doc_topic[i], doc_topic[j]) #cosine computes distance so to compute dist 1 minus
            if dist > 0.6:
                print("%s %s %f"%(i,j, dist))

    #print("{} (top topic: {})".format(names[i], doc_topic[i].argmax()))
