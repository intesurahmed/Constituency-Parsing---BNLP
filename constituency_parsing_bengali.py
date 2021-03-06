# -*- coding: utf-8 -*-
"""Constituency parsing - Bengali.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1be6oXvuZusgXmwFERqi3jc9tIcvdrz5y
"""

import re
#reading file line by line
a_file = open(r"/content/drive/MyDrive/HIN-BEN_Chunk_Sample/Bangla_health_chunk.txt", encoding="utf8")
lines = a_file. readlines()
aList=[]
c=0
for x in lines:
    c+=1
    line1 = x
    #converting [[ to "[[ "
    line1 = line1.replace("[[","[[ ")
    #converting ]] to " ]]"
    line1 = line1.replace("]]"," ]]")
    temp=line1
    # spliting the line1 based on empty string
    temp = line1.split()
    # keeping the first element of temp in Root
    Root=temp.pop(0)
    sentence = "";
    for i in temp:
        # i represent each element of temp
        #spliting i where it founds "\\" and keeping it in word as an array
        word = re.split(r'\\',i)
        #reversing the elements of words
        if word[0]==",":
          word[0]=word[0].replace(',','intesur')
        word.reverse() 
        #merging the elements of the reversed array word
        revStrJoin = ','.join(word)
        if(revStrJoin=="[["):
            continue;

        if(re.search(r']]_',revStrJoin)):
            revStrJoin = revStrJoin.replace(']]_','')
            revStrJoin = '"' + revStrJoin + '"'    
            aList.insert(0,revStrJoin)
            sequence = ",".join(aList)
            sequence =  '(' + sequence + ')'
            if( len(sentence)==0 ):
              sentence = sequence;
            else:
              sentence = sentence + "," + sequence;
            aList.clear()
            

        else:
            revStrJoin = revStrJoin.replace(',','","')
            revStrJoin = '("' + revStrJoin + '")'
            aList.append(revStrJoin)
        
       
    bee='('+'"'+Root+'"'+','+sentence+')'
    #bee=bee.replace('intesur',",")
    #print(bee)
    with open("/content/drive/MyDrive/RA/HIN_BEN_DATASET/Bangla Health.txt", "a") as external_file:
        print(bee, file=external_file)

import svgling
from nltk.tree import Tree
readfile = open(r"/content/drive/MyDrive/RA/HIN_BEN_DATASET/Bangla Tourism.txt", encoding="utf8")
lines = readfile. readlines()
i=0
# converts  nltk tree object to a svg
def tree2svg(t):
    img = svgling.draw_tree(t, global_font_style=styles[0],font_size=styles[1],relative_units=False)
    svg_data = img.get_svg()
    return svg_data
# INSTALL Noto Sans Bengali font in your local machine. Download Font Family from here: https://fonts.google.com/noto/specimen/Noto+Sans+Bengali
styles = ("font-family: \"Noto Sans Bengali\"; font-weight:normal; font-style: normal;", 26)

for line in lines:
  var = line.replace(","," ")
  var = var.replace("\"","")
  i+=1
  var=var.replace('intesur',",") 
  svgling.disable_nltk_png()
  t = Tree.fromstring(var)
  display(t)
  #convert tree to svg
  sv = tree2svg(t)
  file = open('/content/drive/MyDrive/RA/DIAGRAMS/Bengali SVG/Tourism/{}.svg'.format("Bengali Tourism "+str(i)), 'w', encoding='utf-8')
  sv.write(file, pretty=True, indent=2)
  file.close()