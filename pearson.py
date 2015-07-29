import urllib
import urllib2
import json
import settings

#Pearson Credentials
apikey = settings.apikey

Question_1 = "Define me!\n"
# Answer_1 = raw_input(Question_1)
Answer_1 = 'zeus'
#https://api.pearson.com:443/v2/dictionaries/ldoce5/entries?headword=

# https://api.pearson.com/v2/dictionaries/ldoce5/entries?headword=zeus&apikey=lFUBHygWVzco3X4kF9SIHrYQQXHCjPnT
def getword(word):
	baseurl = 'https://api.pearson.com/v2/dictionaries/ldoce5/'
	requrl = baseurl + "/entries?headword=" + word +"&apikey=" + apikey
	resp = urllib2.urlopen(requrl)
	respData = resp.read()
	responseJSON = json.loads(respData)
	#print resp
	print respData
	print "################################################################"
	print responseJSON
	# for x in responseJSON['Entries']['Entry']['multimedia']:
		
		# if x['@type'] == "GB_PRON":
		# 	soundurl = baseurl + x['@href'] + "?apikey=" + apikey
	# return soundurl


print getword(Answer_1)