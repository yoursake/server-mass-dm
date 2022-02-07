import discord
from discord.ext import commands
import os
import colorama 
from colorama import Fore, init
init()
intents = discord.Intents.all()
client =  commands.Bot('<', self_bot = False, intents=intents)
token = input("enter ur token nig: ")
os.system("cls")

@client.event
async def on_ready():
    print(f'''{Fore.YELLOW}
    
    
                           ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
                           ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
                           ██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
                           ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
                           ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
                           ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝for server :)
                           logged in as: {client.user}
                           scrape usage: <scrape [guild id]
                           dmall usage: <dmall

                                                          

    
    
    
    
    
    ''')
@client.command()
async def scrape(ctx, guildid):
    await ctx.message.delete()
    global membercount, guildget
    await client.wait_until_ready()
    guildget = client.get_guild(int(guildid))
    members = await guildget.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as h:
        for member in members:
            h.write(str(member.id) + "\n")
            membercount += 1
            

  
            print(f"Succesfully Scraped {membercount} Members")
@client.command()
async def dmall(ctx, *, text):
  await ctx.message.delete()
  members = open('members.txt')
  for members in ctx.guild.members:
        try:
            
            await members.send(text)
            print(f"{Fore.BLUE}Sent To {members}")
        except:
            pass
client.run(token, bot=True)