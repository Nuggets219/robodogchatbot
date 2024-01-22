"""
DEFAULT VALUES!

debugLogging = False
--False makes everything prettier, True makes it look a bit worse, but gives you the secrets of the universe.
sendMessagesWithAuth = False
--Determines if it uses the user whose token it has and is joined as as a sort of "mouthpiece", outputting messages via
the user.
E.G., if it's my username and token, and this is true, the bot would send messages as me.
target = N/A
--determines the channel the bot connects to. For Twitch, use #(your channel name). ALL LOWERCASE.
possessedUsername = N/A
--Whom to take over. Should be your username, or whoevers' you're using for the bot.
prefix = "[robodoggie] ||"
--the prefix is added onto the front of messages the bot will send. useful if the person the bot is liked to is also
an avid chatter, and you want to tell them apart. just use the quotes with nothing in between for no prefix.
cprefix = ";"
--cprefix stands for Command Prefix. you'd use this in front of a command to call it. Example: ;echo. ; is default to not conflict with other bots.

"""


debugLogging = True
sendMessagesWithAuth = True
target = "#N/A"
possessedUsername = "YOUR USERNAME"
prefix = "[robodoggie] ||"
cprefix = ";"