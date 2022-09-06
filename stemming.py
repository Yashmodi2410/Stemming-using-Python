# Proter Stemming Program:
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
with open('abc.txt', 'r') as f:
    c = f.read()
    a = c.split()
    words = word_tokenize(c)
    for w in words:
        print(w, " ----> ", ps.stem(w))
f.close()


#Snowball Stemming Program
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

snow_stemmer =SnowballStemmer(language='english')

with open('abc.txt', 'r') as f:
    c = f.read()
    words = word_tokenize(c)
    for w in words:
        print(w, " ----> ", snow_stemmer.stem(w))
f.close()

#Lovins Stemming Program
from nltk.tokenize import word_tokenize
from abydos.stemmer import lovins

with open('abc.txt', 'r') as f:
    c = f.read()
    words = word_tokenize(c)
    for w in words:
        print(w, " ----> ", lovins(w))
f.close()
