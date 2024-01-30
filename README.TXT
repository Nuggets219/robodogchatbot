Robodog Chatbot V0.2
last updated 1/29/24

NEW! - Economy module now avaliable at https://github.com/Nuggets219/robodogEcon

USES PYPI (more on that below)
QUICK START GUIDE IS FOR WINDOWS USERS!
-----
ALL THE HEAVY BACKEND LIFTING DONE BY LCOLONQ AND JAKECREATESSTUFF

TURNED INTO THIS TEMPLATE PROGRAM BY NUGGETS219

This code is free for individuals to use, but the IRC function may have some restraints
on coporations using it. Make sure to visit python-irc's webpage for clarification on 
whether you can use it, as i'm no lawyer. Unofficially, it's pretty safe to say that in non-
enterprise applications, such as Twitch streaming, you're pretty safe.
----
The Robodog Chatbot is an IRC-based Twitch chatbot template, made to make it easier for sufficiently knowledgable streamers to host their own chatbots.
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
DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST | DO NOT LOSE THE OAUTH TOKEN | DO NOT SHARE THE OAUTH TOKEN WITH SOMEONE YOU DO NOT COMPLETELY TRUST 
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

----------PROGRAMMING YOUR OWN COMMANDS----------

1. make your program into a function ABOVE the "onEvent" function
definition. i won't give a lecture on Python basics, but if you look at
W3Schools' tutorials and docs, you should get a pretty good idea.
2. add your command to the list in the "onEvent" statement using the following linear flowchart:

Does the command take an "input"?
---
if so, use "in" instead of == in the first section of the 
loop you'll see next. This will check if the command is IN the message, rather
than if the whole message IS the command. this is useful for not triggering the bot on 
those cases where someone goes, "how do I see my..." and you can
freely reply with, "do !(whatever)". I'll probably update this format
to check if the beginning part of the measage matches the command, but until then,
use == or in.
---

Does the command need moderator permission?
---
if so: use the following statement:
elif f"{prefix}your_command" == msg and checkMod(userName) == True:
	your_command()

Note: the f before the quotes and {prefix} are NEEDED if you
want your commands to sync to whatever your prefix is saved as in the config.
If you dont do this, it will be a slight pain in the neck to debug.

Look at the examples i've posted (or will post) and get yourself
acquainted with how it all works. as a very small initial starting project,
I would reccommend adding a command to show a link to your discord, and then add that to your commands list.

so far, guide done.
--------

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EXTRA SUPER DUPER IMPORTANT NOTE:
DO NOT, UNDER ANY CIRCUMSTANCES, USE THE exec() FUNCTION WITH
ANY USER INPUT. This includes even usernames!
This function will execute whatever code is in it, INCLUDING MALICIOUS CODE.
It's easy enough for some scriptkiddie to have your machine print out something
nefarious to chat. LIKE YOUR TOKEN, or address. PLEASE BE SMART.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
