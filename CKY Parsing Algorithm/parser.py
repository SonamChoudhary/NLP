import sys 
grammar_file = sys.argv[1]
sentences_file = sys.argv[2]

def read_grammar():
	grammar={}
	g_file = open(grammar_file,'r').readlines()
	for i in  g_file:
 		i=i.split()
 		if i[0] in grammar:
 			grammar[i[0]].append(i[2:])
 		else:
 			grammar[i[0]]=[i[2:]]
	return grammar

def rule_match(chart1,chart2):
	mapper=[[i,j] for i in chart1 for j in chart2]
	return mapper
	

def parser(sentence):
	rules = read_grammar()
	sentence = sentence.split()
	length =len(sentence)
	row = length 
	col = length
	chart = [[[] for r in range(row)] for c in range(col)]
	col = 0 
	for word in sentence:
		for rule in rules:
			if [word] in rules[rule]:
				chart[col][col].append(rule)
		if (length >1):
			col=col+1
	for c in range(len(sentence)):
		for r in range(c-1,-1,-1):
			for s in range(r+1,c+1,1):
				mapper=rule_match(chart[r][s-1] , chart[s][c])
				for val in mapper:
					for rule in rules:
						if val in rules[rule]:
							chart[r][c].append(rule)
	sentence = map(str,sentence)														
	print "SENTENCE:",sentence
	print "NUMBER OF PARSERS FOUND:",chart[0][-1].count("S")
	print "CHART:"
	for i in range(len(chart)):
		for j in range(len(chart[0])):
			if (chart[i][j] != " "):
				print "\t","chart[%d][%d]"%(i+1,j+1),":",chart[i][j]
	print "\n"				

def main():
	s_file = open(sentences_file,'r').readlines()
	sentence =[]
	for i in s_file:
		sentence.append(i)
	for item in sentence:	
		parser(item)

main()