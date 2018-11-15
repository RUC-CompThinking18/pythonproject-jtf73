#import requests
#url = ("https://api.iextrading.com/1.0/stock/aapl/chart.json")
#import json
    #import simplejson as json
    #parsed_json = json.loads(json_string)
#r = requests.get("https://api.iextrading.com/1.0/stock/aapl/chart")
#print(r)

a = {'prince':'princess'}
b = {'king':50}
c = {1:4}
#Here are a set of dictionaries. There small for now can be messed with.
print (a)
print (b)
print (c)
#Printing here is more to see if it prints the right thing.
for key, value in a.iteritems(): #for val in a:
    if value < 0:
        print ("Fail.")
#            return val
    elif if value > 0:
        print("Check.")
    elif value == 0:
        print("Neutral.")
    else:
        pass
for key, value in b.iteritems(): #for val in b:
    if value < 0:
        print ("Fail.")
#            return val
    elif if value > 0:
        print("Check.")
    elif value == 0:
        print("Neutral.")
    else:
        pass
for key, value in c.iteritems(): #for val in c:
    if value < 0:
        print ("Fail.")
#            return val
    elif value > 0:
        print("Check.")
    elif value == 0:
        print("Neutral.")
    else:
        pass


#Main idea. The code will try to check the dictionary and see if the values in
#said dictionary are positive, negative, neutral, or if values are ints or not.
#Main idea of idead of the code is to run with the api that tracks the stock of
#certain companies, primarily Apple and the like, or book companies. Checking
#their overall change and noting if it's positive or negative. Then saying
#something witty.




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
