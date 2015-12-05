"""
    Tested on python 2.7.7
    For python 3.x some modification are required
    Pre-processing for each use mail send mail data only.

    One More thing that is being not done you can do is NER(named entity recognization)
"""
#Download stopwords using following command if not installed
#nltk.download()

from os import listdir, chdir
import re,sys
from nltk.corpus import stopwords
import nltk
import string
import textmining
import numpy as np
from nltk.stem.porter import *

def hasSpecialCharNum(inputString):
    # - occurs mostly in header-file and phone related text
    # / occurs in dates and url(local and web)
    # : occure in time
    # _ occures in url or line
    # number also removed

    reg = r'\d|-|\\|\_|\:|\-|\~|\=|\~|\*|omni|\.|\'|\/'
    return bool(re.search(reg, inputString))

DATASET_DIR = "/media/mitesh/Personal/Projects/Enron Email Graph Generation/graph_mining/master"

OUTPUT_DIR = "/media/mitesh/Personal/Projects/Enron Email Graph Generation/graph_mining/Pre-Processed"

chdir(DATASET_DIR)
names = [d for d in listdir(".") if "." not in d]
names.remove('stokley-c')
names.remove('harris-s')

stop = stopwords.words('english') 
stop.append("enron")
stop.append("ect")
stop.append("ees")
stop.append("thanks")

for name in names:
    stop.append(name.split("-")[0])    
#print (stop)

stemmer = PorterStemmer()

for name in names:
    sentence_list=""
    word_list = []
    for line in open(DATASET_DIR+"/%s/%s.txt"% (name,name), 'r').readlines():    
        line = line.lower()
        for word in nltk.word_tokenize(line):
            if( len(word) > 2 and word not in stop \
                   and not hasSpecialCharNum(word)):
                word_list.append(word)
     
    sentence_list = ' '.join(word_list)
    out = open( OUTPUT_DIR+"/%s_pre.txt"% name, 'w')
    out.write(sentence_list)
    out.close()
