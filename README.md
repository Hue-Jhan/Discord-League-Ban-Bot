# Discord-League-Ban-Bot
Discord Bot made in Python that mutes, kicks, or bans players who play League Of Legends, Genshin Impact, or Osu, FULLY CUSTOMIZABLE.
Other simply functions and triggers are included.
I used an old PyCharm version, but it makes no difference to use the latest one, i was inspired by this image:

![alt text](https://preview.redd.it/s4vtf394saf81.jpg?width=640&crop=smart&auto=webp&s=08ab633756b0e3ae306f0710760c58ff7d34cfff)


# HOW TO USE
Simply create a discord bot, there are several youtube tutorials you can follow, and upload this codes to your PyCharm specified folder.
You will need to make a new .env file and specify your bot AuthToken, simply create one and type DISCORD_TOKEN=xxxxxxxxxxxxxxxxxxxx

# HOW TO CUSTOMIZE
You will have to replace all of the roles and channels' id of course, you can add as many games you want, and specify what to do once the bot finds a user who plays those games, its all written in the discordmain file. Use the Startwith function because sometimes the name of the game might change in something like "League of legends: lands of idk" so yeah its better to use that function.

Using this bot on multiple server will only allow to kick or ban users, if you want to simply mute them you would have to manage multiple roles, guilds and stuff, but i know how to manage for a single task only, maybe instead you can create mulitple bots, where each one get the IDs for every role and channel you need.

Default mute is set to 1 hour, default cycle to check every user's activity is set to 40 seconds.

How to bypass: simply change your status (bottom left corner of discord gui, not settings) to something else, from what i know the discord API i used cannot tell the difference between someone's activity and someone's status, so if the status is set to anything at all the API will get that, and not the actual user activity, therefore if he is playing one of the banned games he will not be targeted.

# Other Functions
The bot also notifies you whenever a user changes its nickname and specifies the new nickname.

The bot possesses triggers you can customize in the "responses.py" folder (WARNING NSFW CONTENT).
You can customize the bot command to receive personal messages instead of receiving the answer in the channel where you asked it.
The triggers include a rolling dice function.

The bot has also a customizable status (WARNING NSFW CONTENT).
