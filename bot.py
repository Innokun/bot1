import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("ㅎㅇ")

    if message.content.startswith("!설명"):
        await message.channel.send("나는 이노쿤이 2020년 7월8일에 만든 봇이다")        

client.run("NzMwMjc1MjU4OTA0NjA4Nzg5.XwW7eg.hfY9NUk4PGd05n3F8GLYWRU23-g")