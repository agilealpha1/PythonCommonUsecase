import codecs
import fitz,sys
from tika import parser
from pdfminer.high_level import extract_text
import MeCab
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

#os.environ['MECAB_PATH']='/usr/local/lib/libmecab.so'
#os.environ['MECAB_CHARSET']='utf-16'

doc1 ='/Users/Hashiki/Documents/programming/Similarity/install.txt'
wtext ='/Users/Hashiki/Documents/programming/Similarity/install2.txt'

doc2 ='/Users/Hashiki/Documents/programming/Similarity/install2.pdf'
doc3 ='/Users/Hashiki/Documents/programming/Similarity/SecurityTraining2022ja.pdf'
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = codecs.open(doc1,'r','utf-8').read().splitlines()

tagger = MeCab.Tagger('-Owakati')
corpuslist=[tagger.parse(sectence).strip() for sectence in corpus]

vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
transformer = TfidfTransformer()
tf = vectorizer.fit_transform(corpuslist) # 単語の出現頻度を計算
tfidf = transformer.fit_transform(tf) # 各ドキュメントのtfidfを計算

#(文書の数、単語の数)
print(tfidf.shape)

### Target ###
corpusObj = fitz.open(doc3)
out = open(wtext, "wb")  # open text output
"""
for page in corpusObj:
    blocks =page.get_text("blocks")
    blocks.sort(key=lambda b: (b[1], b[0]))
    for b in blocks:
        out.write(b[4].encode("utf-8"))  # write text of page
    #out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()  
"""

#file_data = parser.from_file(doc2)
#text = file_data["content"]

text = extract_text(doc3) 
out.write(text.encode("utf-8"))  # write text of page
out.close()  
print("page contents" , text)

corpusGenTxt = codecs.open(wtext,'r','utf-8').read().splitlines()

corpuslistTarget=[tagger.parse(sectence).strip() for sectence in corpusGenTxt]
sample_tf = vectorizer.transform(corpuslistTarget)
print(sample_tf)
# 本田半端ねぇのTF-IDFを計算する
sample_tfidf = transformer.transform(sample_tf)
# コサイン類似度の計算
similarity = cosine_similarity(sample_tfidf, tfidf)[0]
print(similarity)