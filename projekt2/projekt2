from ascii_graph import Pyasciigraph
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("--size",type=int)
args = parser.parse_args()
filepath = args.filepath
#filepath = "1526_sen_nocy_letniej.txt" 
#filepath = "a-midsummer-nights-dream_TXT_FolgerShakespeare.txt" 
size = 10
if args.size:
    size = args.size


def histogram(list):
  hist =[]
  for x in list:
    hist.append(list.count(x))
  return hist 

def unique(list1, hist_all):
    unique_list = []
    unique_list_hist = []
    i =0
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
            unique_list_hist.append((x, hist_all[i]))
            #hist.append(hist_all[i])
        i = i+1
    return unique_list_hist

#filepath = "1526_sen_nocy_letniej.txt" 
#filepath = "a-midsummer-nights-dream_TXT_FolgerShakespeare.txt" 
f = open(filepath, "rt",encoding="utf-8")
data = f.read()
words = data.split()
print(len(words))
h = histogram(words)
words_hist =unique(words, h)
#print(len(words_hist))
#print(words_hist)

def value(elem):
    return elem[1]

words_hist.sort(key=value, reverse = True)
#print('Sorted list:', words_hist)

graph = Pyasciigraph()
i = 0
for line in  graph.graph('test print', words_hist):
    if(i>size):
      break
    print(line)
    i=i+1

#& C:/Users/Litka/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Litka/Desktop/python_projects/projekt1/projekt1.py 1526_sen_nocy_letniej.txt --size 8
#& C:/Users/Litka/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Litka/Desktop/python_projects/projekt1/projekt1.py a-midsummer-nights-dream_TXT_FolgerShakespeare.txt --size 8