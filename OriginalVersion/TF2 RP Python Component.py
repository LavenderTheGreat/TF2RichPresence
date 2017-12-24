import tkinter.filedialog
import time

writeto = open("./gameinfo.txt","w")
writeto.write("""No IP
Menus
Menu
Menus
Unable to join.""")
writeto.close()

print("""
 OOOO   OOOO
OOOOO   OOOOO
OOOO     OOOO  Team Fortress 2 Rich Prescence!
               Before proceeding make sure you have done the following:
OOOO     OOOO  1 - Read the README
OOOOO   OOOOO  2 - Followed what's in the readme
 OOOO   OOOO   3 - Have a nice mug saying #1 SNIPER on it on your desk and taken one sip out of it.
""")

print("""
Reading config...
""")
print("""
Generating map list...
""")

maps = ("""cp_gravelpit
cp_dustbowl
cp_granary
cp_well
ctf_2fort
tc_hydro
ctf_well
cp_badlands
pl_goldrush
cp_fastlane
ctf_turbine
pl_badwater
cp_steel
cp_egypt_final
cp_junction_final
plr_pipeline
pl_hoodoo_final
koth_sawmill
koth_nucleus
koth_viaduct
ctf_sawmill
cp_yukon_final
koth_harvest_final
ctf_doublecross
cp_gorge
cp_freight_final1
pl_upward
plr_hightower
pl_thundermountain
cp_coldfront
cp_mountainlab
cp_degrootkeep
cp_5gorge
pl_frontier_final
plr_nightfall_final
koth_lakeside_final
koth_badlands
pl_barnblitz
cp_gullywash_final1
cp_foundry
sd_doomsday
koth_king
cp_process_final
cp_standin_final
cp_snakewater_final1
cp_sunshine
cp_metalworks
pl_swiftwater_final1
koth_lazarus
plr_bananabay
pl_enclosure_final
cp_mercenarypark
koth_brazil
cp_mossrock""")
officialmaplist = maps.split("\n")

try:
    pathfile = open("./path.txt", 'r')
    path = pathfile.read()
    path = path.split("\n")
    path = path[0]
    if path == "manual":
        path = tkinter.filedialog.askopenfilename()
        tkinter = 1
    else:
        tkinter = 0
    print(path)
    pathfile.close()
except:
    print("There was an error reading path, going with default path...")
    path = ("C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf")
    print(path)

print("Beginning run loop (Use CTRL C to close or ALT F4)")
run = 1
run2 = 1
found1 = 0
found2 = 0
iteration = 0
while run == 1:
    print ("""
-----------------------------------------------
Iteration """ + str(iteration) + "(" + str(iteration*5) + """secs)
-----------------------------------------------""")
    #logfile = open(path + "console.log", 'r')
    var = 1
    if tkinter == 0:
        logfile = open(path + "/console.log", 'r', encoding='utf-8')
    else:
        logfile = open(path, 'r')
    log = logfile.read()
    log = log.split("\n")
    logfile.close()

    for i in range(0, len(log)-1):
        iteminuse = log[(len(log)-1)-i]
        itemno = (len(log)-1)-i
        if str(iteminuse).startswith("Server Number:"):
            serverno = log[itemno]
            build = log[itemno-1]
            players = log[itemno-2]
            mapname = log[itemno-3]
            servername = log[itemno-4]

            print(serverno)
            print(build)
            print(players)
            print(mapname)
            print(servername)

            found1 = 1
            break
        
    for i in range(0, len(log)-1):
        iteminuse = log[(len(log)-1)-i]
        itemno = (len(log)-1)-i
        if str(iteminuse).startswith("Network:"):
            network = log[itemno]
            #print(network)

            found2 = 1
            iptype = 0
            break
        
    for i in range(0, len(log)-1):
        iteminuse = log[(len(log)-1)-i]
        itemno = (len(log)-1)-i
        if str(iteminuse).startswith("Connecting to "):
            network = log[itemno]
            #print(network)

            found2 = 1
            iptype = 1
            break

    if found1 == 1 and found2 == 1:
        writeto = open("./gameinfo.txt","w")
        head, sep, mapname = mapname.partition("ap: ")
        if iptype == 0:
            head, sep, network = network.partition("etwork: IP ")
            IPadd, sep, network = network.partition(", mode")
            head, sep, network = network.partition(", ports ")
            port, sep, network = network.partition("SV / ")

        if iptype == 1:
            head, sep, network = network.partition("onnecting to ")
            print(network)
            IPadd, sep, network = network.partition("..")
            print(IPadd)
            port = ""

        print("ADDRESS: " + IPadd)
        print("MAP: " + mapname)

        if IPadd.startswith("192.168"):
            IPadd = "localhost or LAN game"

        if mapname in officialmaplist:
            typeofmap = "official"
        else:
            typeofmap = "community"
        
        writeto.write(str(IPadd) + """
""" + str(servername) + """
""" + str(mapname) + """
""" + str(typeofmap) + """
""" + str(port))
        writeto.close()

    time.sleep(5)
            
    
    
