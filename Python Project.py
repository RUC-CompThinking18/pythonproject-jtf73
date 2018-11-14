import requests
url = ("https://api.iextrading.com/1.0/stock/aapl/chart.json")
import json
    #import simplejson as json
    #parsed_json = json.loads(json_string)
r = requests.get("https://api.iextrading.com/1.0/stock/aapl/chart")
print(r)
#aresponse = requests.get()
#def mfdoom(l):
#    l = raw_input("What do you want to talk about?")
    #This takes the users input, mainly the name of coompany's and their stock
    #As long as said company exist, It will print a respnse that continues on the code
#    if l 0: #Will change 0 later
#        print ("Well, I'll tell you what," + l +"ain't dead so they passed step one")

#    print ("The most I can tell you about them is that they're doing fine-wait.")
#    if l("changeOverTime") >= 0 #is a positive increase
    #    print ("Yeah, no, I was right, they're doing pretty well for themselves.")
#    if l("changeOverTime":) < 0 #is a decrease
    #    print ("They're not doing too good nowadays, a bunch of bad choices, a changing market, just not adapting quick enough.")
