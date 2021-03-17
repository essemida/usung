import discord, asyncio 
from pip._internal import commands
import random
client = discord.Client()


@client.event
async def on_ready():
    print("유성이 봇 작동 완료")
    await client.change_presence(status = discord.Status.online, activity = discord.Game('"유성아 도움말" '))
    async def bt(games):
        await client.wait_until_ready()
        await bt(['이름 유성이로 변경함','작동시간보다 오프시간이 더 많을거임'])

         
        while not client.is_closed():
            for g in games:
                await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
                await asyncio.sleep(2)


@client.event
async def on_message(message):
    msg = message.content

    if msg == '유성아':
        await message.channel.send("네!")
    
    if msg == '유성아 안녕':
        await message.channel.send("반가워요!")

    if msg == '유성아 서버':
        await message.channel.send("내가 있는 곳은 델루나 마을, 초승달 왕국, (추가예정)")

    if msg == '유성아 도우미':
        await message.channel.send("저를 만드는걸 도와주신 분은 키시와 코체입니다.")

    if msg == '유성아 은우':
        await message.channel.send("제 짝사랑입니다.")

    if msg == '유성아 랜캐':
        await message.channel.send("랜캐가 누구죠?")

    if msg == '유성아 바보':
        await message.channel.send("응 너네 3대가 탈모")
        
    if msg == '유성아 은우 불러':
    	await message.channel.send(f"<@!{760031684451106846}>")
    	
    if msg == '유성아 관리자 불러':
    	await message.channel.send(f"<@!{783230888342323200}>")

    if msg == '유성아 수령님':
        await message.channel.send("https://tenor.com/view/good-job-kim-jong-un-clapping-north-korea-gif-10867230")

    if msg == '유성아 무야호':
        await message.channel.send("https://tenor.com/view/%EB%AC%B4%EC%95%BC%ED%98%B8-%EB%AC%B4%ED%95%9C%EB%8F%84%EC%A0%84-%EC%95%B5%EC%BB%A4%EB%A6%AC%EC%A7%80-%ED%95%9C%EC%9D%B8%ED%9A%8C%EA%B4%80-%EA%B7%B8%EB%A7%8C%ED%81%BC-gif-20464026")

    if msg == '유성아 서포트 서버':
        await message.channel.send("https://discord.gg/FCYdY6xRBX")

    if msg == '유성아 아잉':
        await message.channel.send("https://cdn.discordapp.com/attachments/814642896909107203/818641930430316564/download.png")

    if msg == '유성아 문':
        await message.channel.send('https://cdn.discordapp.com/attachments/814642896909107203/819117794117156934/DismalJovialGoral-size_restricted.gif')

    if message.content == '유성아 프사':
        await message.channel.send(f"<@!{message.author.id}>")
        embed = discord.Embed(title='여기!', descrition='image embed', color=0xff0000)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/814642896909107203/819496810938105876/artworks-CtLYWZyAvh6GooAy-ucLd3g-t500x500.jpg')
        embed.set_image(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '유성아 도움말':
        embed = discord.Embed(title='이거보고 하면 되', descrition='image embed', color=0x0000ff)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/814642896909107203/819496810938105876/artworks-CtLYWZyAvh6GooAy-ucLd3g-t500x500.jpg')
        embed.set_image(url="https://cdn.discordapp.com/attachments/814642896909107203/819847260644048936/Rainbow.gif")
        embed.set_footer(text='유성아 도움말을 사용해 명령어를 알수 있어요. 유성아 안녕, 서버, 도우미, 아잉, 문, 프사, DM, 개발자, 멘션, 거짓말 탐지기(거탐), 이야기, 서포트 서버, 무야호, 수령님, SMG4(smg4), 바보,프로필')
        await message.channel.send(embed=embed)

    if message.content == '유성아 DM':
            if message.author.dm_channel:
                await message.author.dm_channel.send('ㅇㅋㄷㅋ')
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send('안녕')

    if message.content == '유성아 개발자':
        embed = discord.Embed(title='나를 만드신 분은 SM이다', descrition='image embed', color=0x0ffff00)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/814642896909107203/818707698756878366/486YNCFAFVre8KGYaYBwnqoqmLUAaMhMBoCAE713i2QOCHhAAAAAElFTkSuQmCC.png')
        embed.set_footer(text='SM#3876')
        await message.channel.send(embed=embed)

    if message.content == '유성아 멘션':
         await message.channel.send(f"<@!{message.author.id}>")
         
    if message.content =='유성아 키시':
    	await message.channel.send(f"<@!{602459845534416896}>")
    	
    if message.content =='유성아 역할 멘션':
    	await message.channel.send(f"<@!{814733558945677362}>")

    if message.content == '유성아 거짓말 탐지기':
        ran = random.randint(0,1)
        if ran == 0:
            d = '거짓!'
        if ran == 1:
            d = '진실!'
        await message.channel.send(f"<@!{message.author.id}>")
        await message.channel.send(d)

    if message.content == '유성아 거탐':
        ran = random.randint(0,1)
        if ran == 0:
            d = '거짓!'
        if ran == 1:
            d = '진실!'
        await message.channel.send(f"<@!{message.author.id}>")
        await message.channel.send(d)

    if message.content == '유성아 SMG4':
        ran = random.randint(0,11)
        if ran == 0:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832212857815050/20201102_000948.jpg'
        if ran == 1:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832157190225920/20210213_031423.jpg'
        if ran == 2:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832844259950602/20210129_2144462.jpg'
        if ran == 3:
            d= 'https://cdn.discordapp.com/attachments/814642896909107203/819833453729808404/Screenshot_20210116-1951142.png'
        if ran == 4:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833453951582248/Screenshot_20210212-2040122.png'
        if ran == 5:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454224867337/Screenshot_20210131-1636012.png'
        if ran == 6:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454479802398/20210214_023115.jpg'
        if ran == 7:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454895824916/20210214_023102.jpg'
        if ran == 8:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833455209742386/20210214_023229.jpg'
        if ran == 9:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833455721316362/20210217_002856.jpg'
        if ran == 10:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833456040869908/20210214_023037.jpg'
        if ran == 11:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833456291872778/20210214_023023.jpg'
        await message.channel.send(d)

    if message.content == '유성아 smg4':
        ran = random.randint(0,11)
        if ran == 0:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832212857815050/20201102_000948.jpg'
        if ran == 1:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832157190225920/20210213_031423.jpg'
        if ran == 2:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819832844259950602/20210129_2144462.jpg'
        if ran == 3:
            d= 'https://cdn.discordapp.com/attachments/814642896909107203/819833453729808404/Screenshot_20210116-1951142.png'
        if ran == 4:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833453951582248/Screenshot_20210212-2040122.png'
        if ran == 5:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454224867337/Screenshot_20210131-1636012.png'
        if ran == 6:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454479802398/20210214_023115.jpg'
        if ran == 7:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833454895824916/20210214_023102.jpg'
        if ran == 8:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833455209742386/20210214_023229.jpg'
        if ran == 9:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833455721316362/20210217_002856.jpg'
        if ran == 10:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833456040869908/20210214_023037.jpg'
        if ran == 11:
            d = 'https://cdn.discordapp.com/attachments/814642896909107203/819833456291872778/20210214_023023.jpg'
        await message.channel.send(d)

    if message.content == '유성아 이야기':
        embed = discord.Embed(title='내 이야기를 알려줄게', descrition='image embed', color=0x0000ff)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/814642896909107203/819496810938105876/artworks-CtLYWZyAvh6GooAy-ucLd3g-t500x500.jpg')
        embed.set_footer(text='안녕? 난 유성이 봇이야 내 탄생 이야기를 좀 풀자면 걍 개발자란 놈이 재미로 만들겠다고 날 개발했더라. 근데 한달도 안된 초보자라 그런지 코체랑 키시한테 도움을 요청했어 그렇게..내가 탄생한거지 앞으로도 잘 살아남을순 있을진 모르겠다. 개발자란놈이 코딩에 약간 질리기 시작한면 이젠 나를 관리 안해줄거 같아 ㅋㅋㅋㅋㅋ')
        await message.channel.send(embed=embed)
        
    if message.content =='유성아 프로필':
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉", value=message.author.display_name, inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

     
access_token = os.environ["BOT_TOKEN"]
client.run(access_token) 
