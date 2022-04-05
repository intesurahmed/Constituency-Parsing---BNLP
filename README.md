
# Constituency Parsing Tree - BNLP

Constituency parsing is the process of extracting a constituency-based parse tree from a sentence, which represents the syntactic structure of the sentence using a phrase structure grammar. 

# Bengali Dataset

It has collection of sentences about tourism, entertainment, agriculture and health.
These sentences are arranged in a specific format.

For example: 
HAD9076	[[এই\DM_DMD কুন্ডে\N_NN]]_NP [[বীজের\N_NN কেরা\N_NN পদ্ধতি\N_NN দ্বারা\PSP]]_NP [[বপন\N_NN করা\V_VM_VNG যেতে\V_VM_VINF পারে\V_VM_VF]]_VGF [[৷\RD_PUNC]]_BLK	

# Dataset Preprocessing

To parse it through a python module named svgling, datasets need to be modified. From the raw sentences modified them in a specific order so that sentences can be parsed. To do so need to install some dependencies.

Dependencies: ```pip install svgling```

For example: (Modified raw sentence)

("HAD9076",("NP",("DM_DMD","এই"),("N_NN","কুন্ডে")),("NP",("N_NN","বীজের"),("N_NN","কেরা"),("N_NN","পদ্ধতি"),("PSP","দ্বারা")),("VGF",("N_NN","বপন"),("V_VM_VNG","করা"),("V_VM_VINF","যেতে"),("V_VM_VF","পারে")),("BLK",("RD_PUNC","৷")))

# Tree Forming

Here, used a python module named ```nltk``` to form the parsing table. Installed a dependency ```apt get install -y xvfb``` so that it can display the constituency parsing tree. Installed Bengali font familty so that it can support complex text of Bengali. Then converted the parsing trees into ```.svg```files.

# svg2pngs

Since the goal is to generate ```.png``` of every sentence of the datasets, it needs to install the font family in local PC. To convert the generated ```.svg``` files to ```.png``` files  used nodejs. 