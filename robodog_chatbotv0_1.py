from config import *
from mods import *



global debugLogging, target

with open("token.txt", "r") as f:
    token = f.read().strip()

import random
import irc.client
import logging
import time

if debugLogging is True:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

reactor = irc.client.Reactor()
c = reactor.server().connect("irc.chat.twitch.tv", 6667, possessedUsername, token)


# SHORTCUTS - NUGGETS
def checkMod(user: str) -> bool:
    if user in mods:
        return True
    else:
        return False


def checkTrust(user: str) -> bool:
    if user in superTrusted:
        return True
    else:
        return False


def printToChat(message: str):
    '''quick "n dirty way to output a message to chat. give it a string and it'll output it to chat.'''
    global target
    if sendMessagesWithAuth is True:
        c.privmsg(target, f"{prefix} {message}")
    elif debugLogging is True:
        print("can't send messages if sendMessagesWithAuth = False!")


# END NUGGETS' STUPID SHORTCUTS
# MISC. FUN STUFF- NUGGETS
##LIST COMMANDS
def lsCommands():
    printToChat(f"{cprefix}commands")


##END COMMANDS
##SOCS

def on_event(connection, event):
    global debugLogging, sendMessagesWithAuth
    user = event.source
    userName = user.split("!")[0]
    msg = event.arguments[0]
    if debugLogging is True:
        print((user, msg))
    else:
        print(f"{userName} : {msg}")

    ##IMPORTANT TOOLS - DON'T REMOVE
    if f"{cprefix}debug" == msg and checkMod(userName) is True:
        debugLogging = not debugLogging  # toggle. if debugLogging = True, then it becomes Not True, coloquially known as False. didnt want to write the if-else case lmfao.

        if debugLogging is True:  # switching the cases here because otherwise this command is near pointless.
            logging.basicConfig(level=logging.DEBUG)
            print("Debug on!")
            printToChat("Debug on!")
        else:
            logging.basicConfig(level=logging.INFO)
            print("Debug off!")
            printToChat("Debug off!")
    elif f"{cprefix}debug" == msg and checkMod(userName) != True:
        if debugLogging is True:
            print("!!!!!ABOVE MESSAGE ATTEMPTED TO ACCESS DEBUG W/O DEBUG PERMS!!!!!!!!")
        else:
            print(f"{user} tried to access debug commands without debug perms!")
    elif f"{cprefix}toggleBotChat" == msg and checkTrust(userName) == True:
        sendMessagesWithAuth = not sendMessagesWithAuth
        if sendMessagesWithAuth:
            print("Sending messages to chat is now ON!")
            printToChat("Sending messages to chat is now ON!")
        else:
            print("Sending messages to chat is now OFF!")
            # why print to chat when noone is there
    elif f"{cprefix}toggleBotChat" == msg and checkMod(userName) != True:
        if debugLogging is True:
            print("!!!!!ABOVE MESSAGE ATTEMPTED TO ENABLE/DISABLE POSSESION MESSAGING W/O DEBUG PERMS!!!!!!!!")
        else:
            print(f"{user} tried to access debug commands without debug perms!")
        printToChat(f"{userName} - what are you thinking? You don't have the perms for that!")
    elif f"{cprefix}echo" in msg and userName in mods:
        printToChat(msg.split(f"{cprefix}echo", 1)[1])  # prints everything after the echo command
    elif f"{cprefix}echo" in msg and userName not in mods:
        print(f"{user} is not a mod!")
        printToChat(f"{user} is not a mod!")


    # YOUR PROGRAMS GO HERE------------------------



c.add_global_handler("pubmsg", on_event)
c.join(target)
print("joined")
printToChat("joined successfully!")
reactor.process_forever()
