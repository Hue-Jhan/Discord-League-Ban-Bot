from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
# from discord.ext import commands
from responses import get_response
from discord.ext import tasks
import asyncio
muted_users = {}

# token load
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup
intents: Intents = discord.Intents.all()
intents.message_content = True  # NOQA
intents.members = True  # ignore if it gives u warnings
client: Client = Client(intents=intents)


@tasks.loop(seconds=40)  # Check every x secdonds
async def check_users_activity():
    guild = client.get_guild(1227209424846979094)
    if guild is None:
        return

    for member in guild.members:
        # print(member.activity)
        for activity in member.activities:  # ignore warning
            if member.activity.type == discord.ActivityType.playing:
                game_name = member.activity.name.lower()
                print(member.activity)
                if game_name.startswith("league") or game_name.startswith("genshin") or game_name.startswith("osu"):
                    if member.id not in muted_users:
                        print(f"User {member.name} is playing League, osu or Genshin, not good!")
                        channel = client.get_channel(1227209425060888633)
                        await channel.send(f" {member} your playing haram games, by the power of allah i shall mute you for 1 hour")
                        # await member.kick(" stupid u cant play haram games, get kicked")  command to kick, you can replace "kick" with "ban" to ban instead
                        # await member.send("yo u cant play haram games, get kicked, then think about your actions and join again")    personal message to the user
                        muted_role = guild.get_role(1227209424846979098)
                        await member.add_roles(muted_role, reason="User playing stupid game")
                        unmute_task = asyncio.create_task(lolmute(member))
                        muted_users[member.id] = unmute_task            # comment the previous 4 lines and uncomment the Kick line to just kick the user instead


async def lolmute(member):
    await asyncio.sleep(3600)
    guild = member.guild
    muted_role = guild.get_role(1227209424846979098)
    await member.remove_roles(muted_role, reason="Temporary mute duration elapsed")
    print(f" haram mute time finished for {member}")
    del muted_users[member.id]


@client.event
async def on_member_update(before, after):
    if str(before.nick) != str(after.nick):
        try:
            channel = client.get_channel(1227209425060888633)
            if channel:
                user_name = after.name
                print(f"User {user_name} changed his nigname in {after.nick}")
                await channel.send(f"User {user_name} changed his nigname in \"{after.nick}\" bc he dumb.")
        except Exception as e:
            print(f"An error occurred: {e}")


# messages
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        if response != '0':
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='CUSTOM STATUS', url='https://c.tenor.com/zWTsGa_FBRUAAAAC/tenor.gif'))
    check_users_activity.start()


# incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
