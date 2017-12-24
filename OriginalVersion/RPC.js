//You want to read the RPC.js in map images update first, as it explains alot of this with ease, read it like you count 1 before 2 and watch Phantom Menace before Last Jedi.
//Hence, this has ZERO comments.

var fs = require('fs'); //Import filesystem libraries

const { Client } = require('discord-rpc'); //Create client object from Discord RPC libraries

// Rich Presence only works with IPC, and so it won't work in browser
const client = new Client({ transport: 'ipc' }); //Basic connection establish
global.items = ['s','s','s','s','s']; //Create a basic list, good for placeholders for when no info is found.
async function updatestatus(){ //Define update function
	
	fs.readFile("gameinfo.txt", function (err, data) { //Read file gameinfo
		if (err) throw err; //If it fails, then error
		var data = data.toString(); //Convert file to string
		console.log(data) //Print it for debug info
		global.items = data.split('\n'); //Split it into lines into a list	
    }); //End read.
	
	 
	 console.log(items); //Log list for debug purposes.
	
	
	//code to execute upon update
	if (items[3] == new String("official\r")){ //If the line says that it is an official map.
		global.items //Use global items
		client.setActivity({ //Read the comments on this bit from the other file from map images update!
				state: 'On server: ' + items[1],
				details: '\n Server IP: ' + items[0],
				startTimestamp: Math.round((new Date()).getTime() / 1000),
				endTimestamp: Math.round((new Date()).getTime() / 1000)+15,
				largeImageKey: 'official',
				largeImageText: 'Playing on ' + items[2],
				smallImageKey: 'icon',
				partyId: 'party1234',
				partySize: 1,
				partyMax: 6,
				matchSecret: 'xyzzy',
				joinSecret: 'join',
				spectateSecret: 'look',
				instance: false,
				
		});	
		console.log('UPDATED WITH OFFICIAL')
	
	} else if (global.items[3] == new String("community\r")){
		global.items
		client.setActivity({
				state: 'On server: ' + items[1],
				details: '\n Server IP: ' + items[0],
				startTimestamp: Math.round((new Date()).getTime() / 1000),
				endTimestamp: Math.round((new Date()).getTime() / 1000)+15,
				largeImageKey: 'community',
				largeImageText: 'Playing on ' + items[2],
				smallImageKey: 'icon',
				partyId: 'party1234',
				partySize: 1,
				partyMax: 6,
				matchSecret: 'xyzzy',
				joinSecret: 'join',
				spectateSecret: 'look',
				instance: false,
		});
		console.log('UPDATED WITH COMMUNITY')		
	} else {
		global.items
		console.log(items[0])
		client.setActivity({
			
				state: 'On server: ' + items[1],
				details: '\n Server IP: ' + items[0],
				startTimestamp: Math.round((new Date()).getTime() / 1000),
				endTimestamp: Math.round((new Date()).getTime() / 1000)+15,
				largeImageKey: 'menus',
				largeImageText: 'Playing on ' + items[2],
				smallImageKey: 'icon',
				partyId: 'party1234',
				partySize: 1,
				partyMax: 6,
				matchSecret: 'xyzzy',
				joinSecret: 'join',
				spectateSecret: 'look',
				instance: false,
		});	
		console.log('UPDATED WITH MENUS')
	};
	
	console.log('UPDATED');
}
 

client.on('ready', () => {
	



  
  
  // based on the object from
  // https://github.com/discordapp/discord-rpc/blob/master/examples/send-presence
  console.log('Ready, setting rich presence');
  client.setActivity({
    state: 'Not in a game.',
    details: 'None',
    startTimestamp: Math.round((new Date()).getTime() / 1000),
    endTimestamp: Math.round((new Date()).getTime() / 1000)+15,
    largeImageKey: 'menus',
    smallImageKey: 'icon',
    partyId: 'party1234',
    partySize: 1,
    partyMax: 6,
    matchSecret: 'xyzzy',
    joinSecret: 'join',
    spectateSecret: 'look',
    instance: false,
  });
 
  client.subscribe('ACTIVITY_JOIN', ({ secret }) => {
    console.log('Game Join Request', secret);
  });
 
  client.subscribe('ACTIVITY_SPECTATE', ({ secret }) => {
    console.log('Game Spectate Request', secret);
  });
  
  console.log('starting loop intervals...');
  
  setInterval(updatestatus,1000);
  
});
 
// Log in to RPC with only client id; allows only rich presence.
// If you want to use other features you should see below for an example
// of authorization with scopes, which will still let you use rich presence
// if you are using the `ipc` transport.
client.login(''); //Insert your own client ID here!





