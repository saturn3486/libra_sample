# -*- coding:utf-8 -*-
import feedparser

f = open('output.txt','w')
feed = feedparser.parse("http://ieeexplore.ieee.org/rss/TOC55.XML")
entries = feed['entries']
for entry in entries[:5]:
	print "title:" + entry['title']
	print "link:" + entry['link']
	print "authors:" + entry['authors']

for entry in entries:
	if not entry['authors'] == "":
		f.write("title:" + entry['title']+"\n")
		f.write("link:" + entry['link']+"\n")
		f.write("authors:" + entry['authors']+"\n\n")

f.close()
