from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
	return render(request,'home.html')
	#return render(request,'home.html', {'hithere': 'Welcome'})
	#This html file allows python commands in the form of dictionaries. Do notinclude space in keys.


def chicken(request):
	return HttpResponse('<h1>CHICKEN<h1>')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	wordcount = Counter(wordlist)
	return render(request,'count.html', {'fulltext':fulltext, 'count':len(wordlist), "worddictionary":wordcount.most_common()})

def about(request):
	return render(request,'about.html')