#Python component.

import tkinter.filedialog #Import for manual path option
import time #For sleep functions

writeto = open("./gameinfo.txt","w") #Write defaults in.
writeto.write("""No IP
Menus
Menu
Menus
Unable to join.""") #Default string to write
writeto.close() #End this write process.

print("""
 OOOO   OOOO
OOOOO   OOOOO
OOOO     OOOO  Team Fortress 2 Rich Prescence!
               Before proceeding make sure you have done the following:
OOOO     OOOO  1 - Read the README
OOOOO   OOOOO  2 - Followed what's in the readme
 OOOO   OOOO   3 - Have a nice mug saying #1 SNIPER on it on your desk and taken one sip out of it.
""") #Splash screen.

print("""
Reading config...
""") #Print debug stuff
print("""
Generating map list...
""") #Print debug stuff

officialmaplist = ['arena_badlands', 'arena_granary', 'arena_lumberyard', 'arena_nucleus', 'arena_offblast_final', 'arena_ravine', 'arena_sawmill', 'arena_watchtower', 'arena_well', 'cp_5gorge', 'cp_badlands', 'cp_coldfront', 'cp_degrootkeep', 'cp_dustbowl', 'cp_egypt_final', 'cp_fastlane', 'cp_foundry', 'cp_freight_final1', 'cp_gorge', 'cp_granary', 'cp_gravelpit', 'cp_gullywash_final1', 'cp_junction_final', 'cp_manor_event', 'cp_mercenarypark', 'cp_mossrock', 'cp_mountainlab', 'cp_process_final', 'cp_snakewater_final1', 'cp_standin_final', 'cp_steel', 'cp_vanguard', 'cp_well', 'cp_yukon_final', 'ctf_2fort', 'ctf_2fort_invasion', 'ctf_doublecross', 'ctf_landfall', 'ctf_sawmill', 'ctf_turbine', 'ctf_well', 'koth_badlands', 'koth_harvest_event', 'koth_harvest_final', 'koth_highpass', 'koth_king', 'koth_lakeside_event', 'koth_lakeside_final', 'koth_lazarus', 'koth_nucleus', 'koth_sawmill', 'koth_viaduct', 'koth_viaduct_event', 'mvm_bigrock', 'mvm_coaltown', 'mvm_decoy', 'mvm_ghost_town', 'mvm_mannhattan', 'mvm_mannworks', 'mvm_rottenburg', 'pd_watergate', 'plr_bananabay', 'plr_hightower', 'plr_hightower_event', 'plr_nightfall_final', 'plr_pipeline', 'pl_badwater', 'pl_barnblitz', 'pl_cactuscanyon', 'pl_enclosure_final', 'pl_frontier_final', 'pl_goldrush', 'pl_hoodoo', 'pl_millstone_event', 'pl_snowycoast', 'pl_thundermountain', 'pl_upward', 'rd_asteroid', 'sd_doomsday', 'sd_doomsday_event', 'tc_hydro']
#Above is the list that contains all maps that won't produce a nophoto icon. Changing these will allow you to add maps to the map photo list, in old versions, is used to tell apart community and official maps.
try: #Try to open from a custom log path, if this errors it results to default, luckily.
    pathfile = open("./path.txt", 'r') #Open path file
    path = pathfile.read() #Read it to string
    path = path.split("\n") #Split string into lines to remove junk
    path = path[0] #Grab first line (This contains the path)
    if path == "manual": #If it is manual, open a tkinter dialog
        path = tkinter.filedialog.askopenfilename() #Ditto
        tkinter = 1 #Tell thing it is Tkinter.
    else: # Else...
        tkinter = 0 #... It isn't tkinter, duh.
    print(path) #For debug, print path
    pathfile.close() #Finish read operation
except: #If this fails
    print("There was an error reading path, going with default path...")
    path = ("C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf")
    print(path) #Debug
    #The above details an emergency process to set to the original path.
print("Beginning run loop (Use CTRL C to close or ALT F4)") #Print instructions
run = 1
run2 = 1 #Run loop things.
found1 = 0 #For game info condition
found2 = 0 #for net info condition, these are conditions for finding certain fields in the logfile, as to prevent errors.
iteration = 0 #Broken, sadly. Probably forgot to increment it, stupid me. :D
while run == 1: #Begin run loop
    print ("""
-----------------------------------------------
Iteration """ + str(iteration) + "(" + str(iteration*5) + """secs)
-----------------------------------------------""") #Print iteration and time since launch.
    #logfile = open(path + "console.log", 'r') #Old and useless.
    var = 1 # For conditions, I think.
    if tkinter == 0: #Tkinter conditions
        logfile = open(path + "/console.log", 'r', encoding='utf-8') #Do special parsing for tkinter paths
    else: #else
        logfile = open(path, 'r') #go normal path
    log = logfile.read() #Read the file
    log = log.split("\n") #Split it into a list/
    logfile.close() #Close this operation

    for i in range(0, len(log)-1): #Scan EVERY line of the file in a search for a line that starts with 'Server Number'
        iteminuse = log[(len(log)-1)-i] #It starts from the end of the file, as thats where the most recent stuff will be.
        itemno = (len(log)-1)-i #The line it is reading, since it is in reverse, this is gotten via a calculation.
        if str(iteminuse).startswith("Server Number:"): #Once it finds the server number line, it executes this, the server number line is below all the other needed fields in the TF2 log, so I worked off that.
            serverno = log[itemno]#    \
            build = log[itemno-1]#      \
            players = log[itemno-2]#     } These get the lines from the file that contains all the other info calculated from the line above into variables.
            mapname = log[itemno-3]#    /
            servername = log[itemno-4]#/

            print(serverno)#
            print(build)#
            print(players)#    All this for debug.
            print(mapname)#
            print(servername)#

            found1 = 1 #Say that its found game information.
            break #Break the loops upon discovery.
        
    for i in range(0, len(log)-1): #Scan EVERY line of the file in a search for a line that starts with 'Network'
        iteminuse = log[(len(log)-1)-i] #It starts from the end of the file, as thats where the most recent stuff will be.
        itemno = (len(log)-1)-i #The line it is reading, since it is in reverse, this is gotten via a calculation.
        if str(iteminuse).startswith("Network:"): #The network line contains local IPs, which I didn't know beforehand, I remedy this though later.
            network = log[itemno] #Put network in variable
            #print(network)

            found2 = 1 #Says discovered network ips
            iptype = 0 #Local IP mode, hides ip.
            break
        
    for i in range(0, len(log)-1): #Scan EVERY line of the file in a search for a line that starts with 'Connecting to '
        iteminuse = log[(len(log)-1)-i] #It starts from the end of the file, as thats where the most recent stuff will be.
        itemno = (len(log)-1)-i #The line it is reading, since it is in reverse, this is gotten via a calculation.
        if str(iteminuse).startswith("Connecting to "): #This is finding actual connection info unlike last time.
            network = log[itemno] #Update with new connection info
            #print(network)

            found2 = 1 #Discovered network ips switch
            iptype = 1 #Global IP mode, shows IP
            break

    if found1 == 1 and found2 == 1: #If available IP and other info
        writeto = open("./gameinfo.txt","w")
        head, sep, mapname = mapname.partition("ap: ") #Set map name to everything after 'ap: '
        if iptype == 0:
            head, sep, network = network.partition("etwork: IP ") #cut string
            IPadd, sep, network = network.partition(", mode") #get ip address from cut string
            head, sep, network = network.partition(", ports ") #cut string again
            port, sep, network = network.partition("SV / ") #Get port from cut string

        if iptype == 1:
            head, sep, network = network.partition("onnecting to ")#Set network to everything after 'onnecting to '
            print(network)#debug
            IPadd, sep, network = network.partition("..")#Set IPadd to everything after '..'
            print(IPadd)#debug
            port = ""#blank as not needed

        print("ADDRESS: " + IPadd)
        print("MAP: " + mapname)

        if IPadd.startswith("192.168"):
            IPadd = "localhost or LAN game" #IP hider, so people don't get personal IPs.

        if mapname in officialmaplist:
            typeofmap = mapname #Get map photos if available
        else:
            typeofmap = "none" #Nophoto mode if map not in maplist.
        
        writeto.write(str(IPadd) + """
""" + str(servername) + """
""" + str(mapname) + """
""" + str(typeofmap) + """
""" + str(port)) #Self explanatory, now writes to the file.
        writeto.close() #Finishes operations here.

    time.sleep(5) #Waits five seconds
            
    
    
