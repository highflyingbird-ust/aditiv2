import os
import nltk
from nltk.parse import stanford
from nltk import Tree
from functools import reduce

os.environ['STANFORD_PARSER'] = '/home/sampath/Desktop/stanford/'
os.environ['STANFORD_MODELS'] = '/home/sampath/Desktop/stanford/'

parser = stanford.StanfordParser(model_path="/home/sampath/Desktop/stanford/models/lexparser/englishPCFG.ser.gz")
dep_parser = stanford.StanfordDependencyParser(model_path="/home/sampath/Desktop/stanford/models/lexparser/englishPCFG.ser.gz")

#x = raw_input('Enter text to be parsed: ');
x = 'there is a conclusion to my illusion i assure you this'
dep = list(parser.raw_parse(x))
parsed_sent = str(dep[0])
#print parsed_sent

def binarize(tree):

    if isinstance(tree, str):
        return tree
    elif len(tree) == 1:
        return binarize(tree[0])
    else:
        label = tree.label()
        return reduce(lambda x, y: Tree(label, (binarize(x), binarize(y))), tree)
        
tree = Tree.fromstring(parsed_sent)
bt = binarize(tree)
bt_split = str(bt).splitlines()
print bt

#c = 0
#bt_split_tok = []
#bt_split_strip = []
#label = []
#node = []
#for i in bt_split:
#    j = i.strip()
#    bt_split_strip.append(j)
#    bt_split_tok.append(nltk.word_tokenize(j))    
#    if len(bt_split_tok[c])<3:
#        if bt_split_tok[c][0] == '(':
#            label.append(bt_split_tok[c][1])
#        else:
#            node.append(bt_split_tok[c][0])
#    else:
#        
#    print bt_split_strip[c]
#    print bt_split_tok[c]
#    print '---------------------------------------------------------'
#    c = c+1
#print bt_split_strip
#print bt_split_tok

#index = 0
#pair = []
#for i in parsed_sent:
#    if i == ')':
#        op_index = parsed_sent.rfind("(",0,index)
#        pair.append([op_index,index])
#        parsed_sent = parsed_sent[:op_index] +'X'+ parsed_sent[(op_index+1):]
#    index = index + 1
#
#print pair


        
