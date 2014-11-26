from TwitterAPI import TwitterAPI
import win32com.client
from MSO import *

 # Open PowerPoint
Application = win32com.client.Dispatch("PowerPoint.Application")

# Add a presentation
Presentation = Application.Presentations.Add()

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "e1WhbINIG0betPfLmm16g"
consumer_secret = "JVU8Rhrq9QANJX8rybNhWhEKhqMrU4yqC7yvU2Gxh0"
 
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token_key = "14888261-5JLox5DCiHe7iQRPdJaTb93syK9W8DqZotMy8V5OF"
access_token_secret ="Ws1dUSp5eApbtPggPtOn276t5fM1LgnHiFyVWaylbKsKP"
 
 
# Create a Twitter client 
twitter = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
 

##for tweet in results.get_iterator():
##	print (tweet['id'], tweet['text'])
def draw_tweet(Base, item, pos):
    y = 40 + (pos % 4) * 120
    
    image = Base.Shapes.AddPicture(
        # To get the larger resolution image, just remove _normal from the URL
        item['user']['profile_image_url'].replace('_normal', ''),
        LinkToFile=True,
        SaveWithDocument=False,
        Left=20, Top=y,
        Width=100, Height=100)
    
    try:
        status = item['text'].encode('cp1252')
    except UnicodeEncodeError:
        status = item['text']
    text = Base.Shapes.AddShape(1, 130, y, 460, 100)
    text.Fill.ForeColor.ObjectThemeColor = 2
    text.Fill.ForeColor.Brightness = +0.95
    text.Line.Visible = False
    text.TextFrame.TextRange.Text = status
    text.TextFrame.TextRange.Font.Color.ObjectThemeColor = 3
    text.TextFrame.TextRange.ParagraphFormat.Alignment = 1
    
    user = Base.Shapes.AddShape(9, 600, y, 100, 100)
    user.Fill.ForeColor.ObjectThemeColor = 4
    user.Line.Visible = False
    user.TextFrame.TextRange.Text = '@' + item['user']['screen_name']


Base = Presentation.Slides.Add(1, 12)
    

#query = {'q' : 'Top Chef', 'lang' : 'es', 'count': 100}
results = twitter.request('statuses/filter', {'track': 'blue'})
##for tweet in results.get_iterator():
##	print (tweet['id'], tweet['text'])
	
for pos, item in enumerate(results.get_iterator()):
    draw_tweet(Base, item, pos)
    if pos > 20:
        break
