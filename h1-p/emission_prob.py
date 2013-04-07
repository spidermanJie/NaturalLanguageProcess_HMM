#!/usr/bin/python -tt

import sys
import string 

def emission_prob(filename):
	# add all tag '0' into a dict dict1 
	# add all tag 'I-gene' into a dict dict_gene
	dict1={}
	dict_gene={}
	file = open(filename,'r')
	for line in file:
		line = line.strip()
		p = line.split()
		if 'WORDTAG' in p:
			if p[2]=='I-GENE':
				if(dict_gene.has_key(p[3])):
					dict_gene[p[3]]=dict_gene[p[3]]+1
				else:
					dict_gene[p[3]] = 1 
			elif p[2]=='O':
				if(dict1.has_key(p[3])):
					dict1[p[3]]=dict1[p[3]]+1
				else:
					dict1[p[3]] = 1
	print dict1
	print dict_gene
			
				
def main():
	if len(sys.argv)!=2:
		print 'usage: ./emission_prob.py filename'
		sys.exit(1)
	filename = sys.argv[1]
	emission_prob(filename)
	
if __name__ == '__main__':
	  main()
				
			 