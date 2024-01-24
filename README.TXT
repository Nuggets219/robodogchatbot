Robodog Chatbot V0.1
last updated 1/21/24

USES PYPI (more on that below)
QUICK START GUIDE IS FOR WINDOWS USERS!
-----
ALL THE HEAVY BACKEND LIFTING DONE BY LCOLONQ AND JAKECREATESSTUFF

TURNED INTO THIS TEMPLATE PROGRAM BY NUGGETS219

this code is free for all to use, but if you're a company get your own programmers on this.
-----

the Robodog Chatbot is an IRC-based Twitch chatbot template, made to make it easier for sufficiently knowledgable streamers to host their own chatbots.
Many chatbots nowadays have a lack of customizability- this chatbot has (nearly) infinite, with some technical restrictions (usually brought about by me
being too lazy to implement them.) You can usually work around these, or use the workarounds provided.

This may seem challenging, but don't worry- included in this README is a guide to help you set things up! (As long as you use Windows!)

  ---THE """QUICK""" SETUP GUIDE---

First, install Python. The version should be at least Python 3.12. (https://www.python.org/downloads/)
Once you have installed Python, hit Windows + R, and type "cmd.exe" in the window provided.
Don't be intmidated, this will be easy!
Type EXACTLY: pip install irc
then WAIT! it will look like nothing happens, but unless you get an error, you're fine. It should show a confirmation message.

IF YOU DONT HAVE AN IDE OR AN EQUIVALENT:
I reccommend PyCharm (https://www.jetbrains.com/pycharm/). they're a bit sneaky, so make sure you get the PyCharm Community Edition.
When you install it, find your python.exe file and select it when it asks for an interpreter. Then, close it and right click -> open with -> pycharm this folder.
If pycharm doesn't show up in the "open with" menu, go to the bottom and select to choose another app. Find pycharm.exe and use that.

open EVERYTHING IN THE FOLDER IN PYCHARM or your IDE of choice.
now, we do the initial testing.

in config.py, set the possessed user to your twitch username (all lowercase), and the target to "#(whoever's channel is using this)". If a user
named User1 was the possessed, and the person's chat the bot should be in is User2, config would look like this:
target = "#user2"
possessedUsername = "user1"

If you don't have your USER oauth token:

go to https://twitchapps.com/tmi/. link your twitch account, and copy and paste the oauth token it gives you into token.txt. DO NOT LOSE THIS TOKEN. DO NOT SHOW
IT TO ANYONE YOU DON'T TRUST. SOMEONE WITH YOUR OAUTH TOKEN MAY AS WELL HAVE YOUR ENTIRE ACCOUNT. BE SMART.
again:

DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST |

IF YOU HAVEN'T, paste this oauth token into token.txt.

Now go back to your config file, and modify that to your liking. descriptions of what everything does should be included. Note that the next step could be a bit easier
if you enable debugLogging.

Go to the mods file, and enter your mods' names AND YOURS into the list - for example:
mods = ["mod1","mod2","mod3"...]


Once you're done, save your modifications to the files, and run robodog_chatbotv0_1.py.
if you did everything right, it should say "joined", and subsequently start printing out messages sent in the channel.
use your chosen command prefix (; is the default) and echo to send a message with the bot:
;echo test
[robodoggie] || test
Now, you're ready to start making your own programs for the bot!
Standard python is fully supported - just make sure you look at the other programs so you know what to do!
use userName and msg when getting the senders' username and message!

I may update these docs later, until then, have fun!
