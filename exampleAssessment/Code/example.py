#!/usr/bin/env python3	
def example1(x):
	odd_list = []
	even_list = []
	x = x.split(" ")
	for n in x:
		n=int(n)
		if n%2 == 0:
			even_list.append(n)
		else:
			odd_list.append(n)
	if len(odd_list)==1:
		return x.index(str(odd_list[0]))+1
	return x.index(str(even_list[0]))+1
def example2(s):
	s = s.split(" ")
	shortest = s[0]
	for word in s[1:]:
		if len(word) < len(shortest):
			shortest = word
	return len(shortest)
def example3(l):
	list_out = []
	for i in l:
		if isinstance(i,int):
			list_out.append(i)
	return list_out