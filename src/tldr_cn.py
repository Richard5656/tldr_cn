# !python3
import re
import sys
import time
import requests
from googletrans import Translator

class Page(object):
	"""don't know how to explain the class"""
	def __init__(self):
		self.title = ""				
		self.explains = []
		self.commands = []
		
	def requestForTldr(self, command):
	    
	    url = "https://raw.githubusercontent.com/tldr-pages/tldr/master/pages/common/{}.md".format(command)

	    i = 0
	    while i < 10:
	        try:
	            time.sleep(i)
	            r = requests.get(url, timeout = 1) 
	            if r.status_code == 200:
	                return r.text
	            else:
	                print("not found the command ")
	                return ""
	        except Exception as identifier:
	            print("warning", end = ":")
	            print("time out when requests")
	        
	            if i == 9:
	                print("have try 10 times , give up !")
	                return ""
	            else:
	                pass
	        i = i + 1

	def parseText(self,text):
		self.title = re.search(">[\s\S]*.",text).group()	
		self.explains = re.findall("-[\S\S]*:",text)
		self.commands = re.findall("`[\s\S]*`", text)

	def trans(self,text):
		i = 0	
		while i < 6:
			try:
				time.sleep(i)
				translate = Translator()
				result = translate.translate(text,dest="zh-CN")
				return result.text
			except Exception as e:
				print("exception when trans")
			i = i + 1

	def go(self, cmd):
		text = self.requestForTldr(cmd)
		print("requests finish")
		self.parseText(text)
		print("parse text ok")

		t = self.trans(self.title)
		print(t)

def main():

	page = Page()
	if len(sys.argv) < 2:
	    page.go("cd") 
	elif len(sys.argv) > 2:
	    print("only receive one args")
	else:
		page.go(sys.argv[1])

if __name__ == '__main__':
	main()
