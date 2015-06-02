# -*- coding:utf-8 -*-

import feedparser

f = open('output_JJAP.txt','w')
"""お次は JJAPのRSS行ってみよう。"""
target_url = "http://iopscience.iop.org/1347-4065/?rss=1"
feed = feedparser.parse(target_url)
entries = feed['entries']

"""確認用にちょっとつまみ食い"""
for entry in entries[:3]:
  print "title:" + entry['title']
  print "link:" + entry['link']

"""今回のXLMでは、title,authorの所にユニコード野郎が隠れてやがったので、asciiに変換して取り込む。"""
for entry in entries:
	if not entry['authors'] == "":
	  f.write("title:" + entry['title'].encode('ascii', 'ignore') + "\n")
	  f.write("link:" + entry['link'] + "\n")
	  f.write("authors:" + entry['author'].encode('ascii', 'ignore') + u"\n\n")

f.close()
