#Import modules and stuff for tracking
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import configV
import time


################### Keys ##################
ckey =configV.values["ckey"] 
csecret =configV.values["csec"]
atoken = configV.values["otoken"]
asecret = configV.values["osec"]

class listener(StreamListener):

    def on_data(self, data):
        try:
		#print data
		''' split up the data '''
		tweet = data.split(',"text":"')[1].split('","source')[0]
		print tweet
		saveThis = '' + tweet
		saveFile = open('twitdb2.csv','a')
		saveFile.write(saveThis)
		saveFile.write('\n')
		saveFile.close()
		return True
	except BaseException, e:
		print 'failed on data',str(e)
    		time.sleep(2)
	def on_error(self, status):
       		 print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[""])

