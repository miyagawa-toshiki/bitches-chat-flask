from janome.tokenizer import Tokenizer
import re
def Negative(txt):
    re_and = re.compile(' &[ !]')
    PATH = 'pn.csv.m3.120408.trim'
    with open(PATH) as fd:
        word_dict_noun = {}
        for line in fd:
            word, polarity, word_type = line.split('\t')
            if polarity == 'e':
                continue
            #word = neologdn.normalize(word)
            word_dict_noun.update({word: polarity})
    t = Tokenizer()
    tokens = t.tokenize(txt)
    docs = []
    for token in tokens:
        if token.part_of_speech.split(',')[0] in ['名詞']:
            docs.append(token.surface)

    point=0
    for word in docs:
        if word in word_dict_noun:
            negaposi = word_dict_noun[word]
            if negaposi == 'n':
                point += 1
            elif negaposi == 'p':
                point -= 1
            else:
                point += 0
    return point
