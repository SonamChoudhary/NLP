#HW-3 Programming
import sys 
import math
from operator import itemgetter
seeds_file = sys.argv[1]
contexts_file = sys.argv[2]
dict_context = {}

def create_avg_log(candidate_list,dict_context,list_seed):
	new_candidate_list = [item for item in candidate_list if item not in list_seed]
	total =0
	list_avg =[]
	for i in new_candidate_list:
		total_z =0
		count_pattern_match=0
		z=0
		for key in dict_context:
			count_match = 0
			y=0
			if (i in dict_context[key]):
				count_pattern_match+=1
				count =0
				for seed_wrd in list_seed :
					if (seed_wrd in dict_context[key]):
						count +=1
				y+=count 
			z+= math.log(y+1,2)
		total=count_pattern_match
		avg=float(z)/total
		avg = format(avg,'.3f')
		list_avg.append([i,avg])
	list_avg.sort(key=lambda x: float(x[1]),reverse = True)
	sort_list_alpha = sorted(list_avg,key=itemgetter(0))
	list_avg = sorted(sort_list_alpha,key=itemgetter(1),reverse = True)
	print "NEW WORDS"
	for i in range(5):
		print list_avg[i][0].lower(),"(",list_avg[i][1],")"
		list_seed.append(list_avg[i][0].strip())
	print "\n"
	return list_seed
						
def create_candidate_list(pattern_pool,len_pool,dict_context,list_seed):
	temp_candidate_list = []
	new_list_seed =[]
	for i in range(len_pool):
		temp_candidate_list.append(pattern_pool[i][1])
	candidate_list=[item for candidate_list in temp_candidate_list for item in candidate_list]
	candidate_list =list(set(candidate_list))
	new_list_seed=create_avg_log(candidate_list,dict_context,list_seed)
	return new_list_seed

def calculate_RlogF(key,count,total_freq):
	x = float(count)/total_freq
	y=math.log(total_freq,2)
	RlogF=x*y
	RlogF = format(RlogF,'.3f')
	return RlogF

def create_pattern_pool(list_seed,dict_context):
	for key in dict_context:
		count = 0
		total_freq = len(dict_context[key])
		for seed_wrd in list_seed:
			if (seed_wrd in dict_context[key]):
				count += 1
		rlogF=calculate_RlogF(key,count,total_freq)
		dict_context[key].append(rlogF)
	list_pool = [[k,v] for k,v in dict_context.items()]
	list_pool.sort(key=lambda x: float(x[1][-1]),reverse = True)
	i=10	
	y=0
	while (list_pool[i][1][-1] == list_pool[i-1][1][-1]):
		i+=1
		y+=1
	return list_pool[0:10+y],10+y
	
def read_context_dictionary():
	with open(contexts_file) as f:
    		context = [i.strip().split('*') for i in f]
	for list_i in context:
		key = str(list_i[1])
 		val = list_i[0]
 		val = val.split()
 		#print val
 		if key in list(dict_context.keys()):
 			dict_context[key].append(val[-1])
 			dict_context[key]=list(set(dict_context[key]))
 		else:
 			dict_context[key] = [val[-1]]
 			dict_context[key]=list(set(dict_context[key]))
	return dict_context

def read_seed_file(): 
	list_seed_word = []  
	with open(seeds_file) as s:
		seed = s.readlines()
		for i in seed :
			i=i.upper()
			list_seed_word.append(i.strip())
	return list_seed_word

def main():
	dict_context = {}
	pattern_pool =[]
	list_seed = read_seed_file()
	dict_context = read_context_dictionary()
	new_list_seed =[]
	temp_pattern_pool =[]
	print "Seed Words:",
	for wrd in list_seed:
		print wrd.lower(),
	print "\nUnique patterns: " ,len(dict_context.keys())
	for i in range(5):
		list_set=[]
		if (len(new_list_seed) != 0):
			list_seed = list(new_list_seed)
		pattern_pool,len_pool=create_pattern_pool(list_seed, dict_context)
		print "\nITERATION",i +1
		print "\nPATTERN POOL"
		for j in range(len(pattern_pool)):
			[a,b] = pattern_pool[j][0],pattern_pool[j][1][-1]
			list_set.append([a,b])
		list_set.sort(key=lambda x: float(x[1]),reverse = True)
		sort_list_alpha = sorted(list_set,key=itemgetter(0))
		list_set = sorted(sort_list_alpha,key=itemgetter(1),reverse = True)
		for i in range(len(list_set)):
			print i+1,".",list_set[i][0],"(",list_set[i][1],")"
		print "\n" 
		for value in dict_context.values():
			del value[-1]
		new_list_seed=create_candidate_list(pattern_pool,len_pool,dict_context,list_seed)
		
main()

