import sys
dictionary_file = sys.argv[1]
rules_file = sys.argv[2]
test_file = sys.argv[3]
global count
count = 0 
global found
found = False
#----------------------------------------Dictionary--------------------------------------------------------
def create_dict():
  list_k = []
  list_v = []
  list1 = open(dictionary_file,'r').readlines()
  for line in list1:
    line=line.lower()
    list_1 = line.split()
    key = list_1[0].lower()
    value = list_1[1:]
    list_k.append(key)
    list_v.append(value)
  return list_k,list_v
  
list_key,list_val = create_dict()
global dict_y
dict_y=dict(zip(list_key,list_val))
l=0
k=l
for i in list_key:
  k=k+1
  for j in list_key[k:]:
   if i==j: 
    z=list_key.index(i)

    dict_y[i].extend(list_val[z])
#-------------------------------------------Search after applying rules------------------------------

def morp_dict_search(wrd,list_r,list_f,list_3_prev,list_5_prev,):
  if wrd in dict_y:
    found=True
    val = dict_y[wrd]
    if list_3_prev == "": 
      if "root" in dict_y[wrd]:
        print test_word, list_f, "ROOT=",dict_y[wrd][dict_y[wrd].index("ROOT")+1], "SOURCE= MORPHOLOGY\n"
      else:
        print test_word, list_f, "ROOT=",wrd, "SOURCE= MORPHOLOGY\n" 
    elif (list_3_prev != ""):
      if(list_3_prev == list_f):
        if "root" in dict_y[wrd]:
          print test_word, list_5_prev, "ROOT=",dict_y[wrd][dict_y[wrd].index("ROOT")+1], "SOURCE= MORPHOLOGY\n"
        else:
          print test_word, list_5_prev, "ROOT=",wrd, "SOURCE= MORPHOLOGY\n"
    #return word_found_in_dict
  else:
    found = False
    morph_analy(wrd,list_r,list_f) 

#------------------------------------------------Applying rules-Analyser----------------------------------------

def morph_analy(x,list_3,list_5):
  #word_found_in_dict=False
  global count
 # if_found = False
  file_rule = open(rules_file,'r').readlines()
  for i in file_rule:
    i=i.lower() 
    list_rule = i.split() 
    if list_rule[0] == "suffix" and str(x).endswith(list_rule[1]):
      if list_rule[2].isalpha(): 
        suff_len=len(list_rule[1])
        wrd_srch = x[:-suff_len]
        rep_len = len(list_rule[2])
        wrd_srch = wrd_srch + list_rule[2]
        count +=1
        if(list_3 != "") and (list_3 != list_rule[5]):
          break 
        else:
         morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)
          
        #morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)

      else:
        suff_len=len(list_rule[1])
        wrd_srch = x[:-suff_len]
        count +=1
        if(list_3 != "") and (list_3 != list_rule[5]):
          break
        else:
          morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)  
        #morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)
     
    elif list_rule[0] == "prefix" and str(x).startswith(list_rule[1]):
      if list_rule[2].isalpha() == True: 
        pref_len=len(list_rule[1])
        wrd_srch = x[pref_len:]
        rep_len = len(list_rule[2])
        wrd_srch =list_rule[2] + wrd_srch
        count +=1
        if(list_3 != "") and (list_3 != list_rule[5]):
          break
        morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)
      else:
        pref_len = len(list_rule[1])
        wrd_srch = x[pref_len:]
        count +=1
        if(list_3 != "") and (list_3 != list_rule[5]):
          break
        morp_dict_search(wrd_srch,list_rule[3],list_rule[5],list_3,list_5)
  if x == test_word and count == 0   :
    print test_word,"noun", "ROOT=",test_word, "SOURCE= Default\n"
     
 
#------------------------------------------dictionary search-----------------------------------------------
list_t =open(test_file,'r').readlines()
for i in list_t: 
  check_y=i.strip("\n")
  check_i=check_y.lower()
  if check_i in dict_y:  
    if "ROOT" in dict_y[check_i]:
      print check_i, dict_y[check_i][0], "ROOT=",dict_y[check_i][dict_y[check_i].index("ROOT")+1], "SOURCE= Dictionary\n"
    else:
      print check_i, dict_y[check_i][0], "ROOT=",check_i, "SOURCE= Dictionary\n"
  else:
    list_3 = ""
    list_5 = ""
    global test_word
    test_word = check_i
    found =False
    morph_analy(check_i,list_3,list_5)
if found == False and check_i != "":
  print check_i,"noun", "ROOT=",test_word, "SOURCE= Default"


  
  











 




  
