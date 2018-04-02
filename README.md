# TF2RichPresence

A commented, easily accessible version of the latest TF2 Rich Presence mod (https://gamebanana.com/gamefiles/6170)

## What diffrentiates this from other versions?

It contains all image files, for a start, has all Client IDs removed and is all commented (Only for the Map Photos update, sorry about that)

## What do I have to abide by to use this?

Just a simple give credit where needed, ie. link here or to my GameBanana profile when you use this source code.

## Setup

###  Setting up a developer app to use this:
1. Go to [here](https://discordapp.com/developers/applications/me)
2. Click 'New App'
3. Type a name, this is in BOLD above the status and is the game name, so nothing technical (Mine was initially TF2 RPC before realising this and changing it to 'Team Fortress 2')
4. Set an icon, just makes it easier to see on the apps page and also pass in a description too, just useful for you as the developer.
5. Jot down your Client ID, you need this to connect with your scripts.
6. Click 'enable rich presence', NOTE: YOU DO NOT NEED TO INVITE TESTERS
7. Set a cover image, I think this is only used for invites so you probably don't need it but its for completeness sake.
8. Upload images! The name you set is what you need to set as largeimagekey or smallimagekey to have that display. Small images cannot be used as large images and large images cannot be used as small images.

You are now ready to go! Please use this wisely and as said before GIVE CREDIT!

### Setting up software

1. Get Node.JS : https://nodejs.org/en/ (Just get LTS version)
    * NPM needs Git, so go get GIT at https://git-scm.com/downloads
2. Install it
3. Open CMD (Windows key, type CMD, click first result)
4. Type 'npm install --save discord.js' without quotes
5. Type 'npm install discord-rpc'
    * Get Python from here (Recommended - https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64-webinstall.exe): https://www.python.org/downloads/release/python-363/
6. Close CMD
7. Open Steam
8. Right click Team Fortress 2, properties, set launch options..., then type -condebug, close it.
9. Put the path to your TF folder in path.txt, typically 'C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf', follow the instructions in path.txt
10. Run the python file (`python tf2RpPythonComponent.py`)
11. Run the launcher.bat file
12. Done!

Just close all windows when done :clap: and if it still shows you playing TF2, close all CMD windows or CTRL R on discord.

*Hope you enjoy this, oh and anyone who manages to package/freeze this, contact me on gamebanana and we can sort something out!*

## Path settings

`C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf`

`/home/[USER]/.local/share/Steam/steamapps/common/Team Fortress 2/tf`

This should be the path to your TF folder, where console.log resides. This path should not contain any \ s and if those do exist they should be replaced with /s.

>*EXAMPLE: C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf*

If this is empty it will use a default path.

If you are fussy and change the path everytime, this can contain 'manual', which opens a file dialog, but also leaves a laggy Tkinter window open
