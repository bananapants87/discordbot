import discord, responses, requests, keyring
from discord.ext import commands

token = keyring.get_password("discord token", "token")
intents = discord.Intents.all()
intents.members = True
#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

async def send_message(message, user_message, is_private):
    
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
def run_discord_bot():
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
            
        if user_message[0:11] == "!dictionary":
            try:
                await message.channel.send(responses.dictionary(user_message))
                
            except Exception as e:
                print(e)
           
        if user_message[0:8] == "!synonym":
            try:
                await message.channel.send(responses.synonym(user_message))
                
            except Exception as e:
                try:
                    await message.channel.send(responses.synonymOffensive(user_message))
                    
                except Exception as e:
                    print(e)
                    
                print(e, "\nPossible offensive word.")

    client.run(token)