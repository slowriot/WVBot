WVBot
=====
This is an IRC bot built in Python using the asynchronous networking library in Tornado.  The bot
was built for the Tardis Project's (http://www.tardis.ed.ac.uk) IRC channel where if you suggest
something that needs to be done you will likely be told "Well Volunteered" (i.e. Go and do it then).

The bot reads messages being said in the channel and if one is matched as someone suggesting
something, it will respond with "Well Volunteered!" and tell the user how many things they have
volunteered to do.  The messages where the user volunteers something are logged in a database.

**WVBot requires Python 3**

Installation
------------
* Install all dependencies listed in requirements.txt
* Create a copy of config.ini.sample and call it config.ini
* Set up config.ini with settings to connect to your database and IRC server/channel
* Start the bot by executing the wvbot.py file