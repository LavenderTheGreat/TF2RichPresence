var fs = require('fs'); //Import filesystem libraries
const { Client } = require('discord-rpc'); //Create client object from Discord RPC libraries

// Rich Presence only works with IPC, and so it won't work in browser
const client = new Client({ transport: 'ipc' }); //Basic connection establish
global.items = ['s','s','s','s','s']; //Create a basic list, good for placeholders for when no info is found.
async function updatestatus() { //Define update function

	fs.readFile("gameinfo.txt", function (err, data) { //Read file gameinfo
		if (err) throw err; //If it fails, then error
		var data = data.toString(); //Convert file to string
		console.log(data) //Print it for debug info
		global.items = data.split('\n'); //Split it into lines into a list
    }); //End read.

	console.log(items); //Log list for debug purposes.

	//code to execute upon update
	if (items[3] == new String("none\r")){ //If the icon line declares it is a special class (Like none), execute code which sets icon to none
		global.items //Use items global
		client.setActivity({ //Send activity to Discord
				state: 'On server: ' + items[1], //Set status to 'On server: '+ server gamemode line
				details: '\n Server IP: ' + items[0], //Set subtext to 'IP: ' + the ip line
				startTimestamp: Math.round((new Date()).getTime() / 1000), //Set the time to the current time
				endTimestamp: Math.round((new Date()).getTime() / 1000)+15, //Set the time limit to 15 seconds ahead (When the RP updates, in other words)
				largeImageKey: 'nomapphoto', //Say that there is no image, remember to make it an image that is present in your app on discordapp
				largeImageText: 'Playing on ' + items[2], //Set largeImageText to 'playing on:' + map name
				smallImageKey: 'icon', //Set small image to the image labelled icon
				smallImageText: 'TF2 Rich Presence by LavenderTheGreat', //Set the small image text to the string
				partyId: 'party1234', //For completeness sake
				partySize: 1, //For completeness sake
				partyMax: 6, //For completeness sake
				matchSecret: 'xyzzy', //For completeness sake
				joinSecret: 'join', //For completeness sake
				spectateSecret: 'look', //For completeness sake
				instance: false, //For completeness sake

		});
		console.log('UPDATED WITH NONE') //Log for debug

	} else { //If not listed as 'nophoto' in the file...
		global.items //Use items global
		console.log(items[0]) //For debugging, self explanatory
		client.setActivity({ //Send activity to Discord
				state: 'On server: ' + items[1], //Set status to 'On server: '+ server gamemode line
				details: '\n Server IP: ' + items[0], //Set subtext to 'IP: ' + the ip line
				startTimestamp: Math.round((new Date()).getTime() / 1000), //Set the time to the current time
				endTimestamp: Math.round((new Date()).getTime() / 1000)+15, //Set the time limit to 15 seconds ahead (When the RP updates, in other words)
				largeImageKey: items[3].replace("\r", ""), //Also bears old carriage return replacer like below. Finds the map line and puts in the string from that to discordapp for the large image (eg. map line is 'ctf_2fort', image displayed would be one labelled 'ctf_2fort' on your app.
				largeImageText: 'Playing on ' + items[2].replace("\r", ""), //Set largeImageText to 'playing on:' + map name, this retains old code to remove carriage returns at the end, so you can remove that
				smallImageKey: 'icon', //Set small image to the image labelled icon
				smallImageText: 'TF2 Rich Presence by LavenderTheGreat', //Set the small image text to the string
				partyId: 'party1234', //For completeness sake
				partySize: 1, //For completeness sake
				partyMax: 6, //For completeness sake
				matchSecret: 'xyzzy', //For completeness sake
				joinSecret: 'join', //For completeness sake
				spectateSecret: 'look', //For completeness sake
				instance: false, //For completeness sake
		});
		console.log('UPDATED WITH SPECIAL') //Log for debug
	};
	console.log('UPDATED'); //Log for debug
}


client.on('ready', () => { //When client is ready...
  // based on the object from
  // https://github.com/discordapp/discord-rpc/blob/master/examples/send-presence
  console.log('Ready, setting rich presence'); //For debug
  client.setActivity({ //Set default presence
    state: 'Not in a game.', //Main text set to not in a game
    details: 'None', //Subtext set to none
    startTimestamp: Math.round((new Date()).getTime() / 1000), //Set the time to the current time
    endTimestamp: Math.round((new Date()).getTime() / 1000)+15, //Set the time limit to 15 seconds ahead (When the RP updates, in other words)
    largeImageKey: 'menus', //Set the large image to 'menus'
    smallImageKey: 'icon', //Set the small image to 'icon'
    partyId: 'party1234', //For completeness sake
    partySize: 1, //For completeness sake
    partyMax: 6, //For completeness sake
    matchSecret: 'xyzzy', //For completeness sake
    joinSecret: 'join', //For completeness sake
    spectateSecret: 'look', //For completeness sake
    instance: false, //For completeness sake
  });

  client.subscribe('ACTIVITY_JOIN', ({ secret }) => { //For completeness sake
    console.log('Game Join Request', secret); //For completeness sake
  }); //For completeness sake

  client.subscribe('ACTIVITY_SPECTATE', ({ secret }) => {  //For completeness sake
    console.log('Game Spectate Request', secret); //For completeness sake
  }); //For completeness sake

  console.log('starting loop intervals...'); //Log for debug
  setInterval(updatestatus, 1000); //Update each 10 seconds (Note to self: Why 10 seconds?)
});

// Log in to RPC with only client id; allows only rich presence.
// If you want to use other features you should see below for an example
// of authorization with scopes, which will still let you use rich presence
// if you are using the `ipc` transport.

client.login(''); //Put in the client ID from your page here, mine is relatively private, but you can get it anyway from the release on GB, please don't abuse.





