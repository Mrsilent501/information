import os
try:
	from bs4 import BeautifulSoup as bs
except:
	os.system("pip install bs4")
try:
	import requests
except:
	os.system("pip install requests")
try:
	import socket
except:
	os.system("pip install socket")
import sys
from time import sleep
os.system("clear")
################################################################
plan = """
      \033[96m< \033[91melectronic deterrent army \033[96m>
\033[1m\033[91m#%%\033[30m$%$#%#$#$%#$%#$%#$$$%#%$%#$%% \033[96mS
\033[91m#$%@#$@\033[30m#%@#%$#@#$@#%@#$@#$@#$%%# \033[96mI
\033[91m#%$!#@%$@%%$\033[97m#@@$#@#$@#%@#@$@#%@$ \033[96mL
\033[91m#@$@#%%$@%@#\033[97m$@#%@#%@#$@#%@#%@%#@ \033[96mE
\033[91m#%$@#%@\033[32m#$@#$@#%@#$@#$@#%@#$@#$@# \033[96mN
\033[91m$#$%\033[32m#$%#$%#$%#$%#$%#$%#$%#$%#$%% \033[96mT
       \033[96m< \033[91melectronic deterrent army \033[96m>
"""
def banner():
	for s in plan:
		sys.stdout.write(s)
		sys.stdout.flush()
		sleep(0.01)
banner()
################################################################
url = "https://who.is/domains/search"
ip = str(input("\n\033[92m[\033[94m+\033[92m] \033[96mEnter \033[91mIP \033[96mor \033[91mDomin \033[96mTo Start --> \033[96m"))
try:
	data = {
	"searchString": ip
	}
	req = requests.post(url, data=data).text
	soup = bs(req, "html.parser")
	find = soup.find_all("div", {"class":"col-md-12 queryResponseBodyKey"})
	for i in find:
		os.system("clear")
		banner()
		print ("\n\033[92m[\033[94m+\033[92m] \033[91mInformation \033[96m<>")
		print ('\033[92m' + i.text)
################################################################
except:
	print ("\033[91m[\033[92m?\033[91m] \033[91mError \033[94m<>")

