import discord
import time

import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def yontem(ctx):
    await ctx.send(f'Hey! Çevreyi korumak hakkında bilgi mi istersin? nereden başlayacağını mı bilmiyorsun? o zaman doğru yere geldin! sana bunu teker teker anlatacağım!')
    time.sleep(2)
    await ctx.send(f'Şimdi ilk olarak yapman gereken çevrendekilerde farkındalık yaratmak! kendi başına bu dünyanın süper kahramanı olacağını mı sanıyorsun? Bu yanlıştır! Tabi zengin değilsen')
    time.sleep(2)
    await ctx.send(f'İlk olarak çevrendekilere anlat! Söyle! Paylaş! ve onlarda farkındalık yarat ve birlikte tartışın konuşun!')
    time.sleep(2)
    await ctx.send(f've ikinci olarak eyleme geçiş yapman lazım... Kendi hedefinizi gerçekleştirmek! Bir fikir üzerinde konuşan ve değinen çoktur... ama düzelten ciddi derecede azdır...')
    time.sleep(2)
    await ctx.send(f'Eylem olarak ne yapmak istediğinizi gerçekleştirmeye başlayın... ne fikir mi istiyorsunuz? sadece $fikir yazın yeter!')
    time.sleep(2)
    await ctx.send(f'Fikri yaptınız ve gerçekleştirdiniz... şimdi üçüncü olarak bunu büyütmeniz gerek... bunun için gönüllü toplayabilirsiniz veya yakınınızdaki şirketlere hedefinizden bahsedin... Eğer şirket bunun gibi sorunlarla uğraşıyorsa sizin teklifinizi kabul edebilir! ve en azından şehir için tanınma kazanmış olursunuz!')
    time.sleep(2)
    await ctx.send(f'bundan sonra şirketinizi ülke dışı tüm dünyada yayınlayabilirsiniz! Bunun için kampanyalar düzenleyebilir ünlülerle iletişime geçebilirsiniz!')
    time.sleep(2)
    await ctx.send(f'bundan sonra... neyse ne biliyim istediğinizi yapın...')

@bot.command()
async def fikir(ctx):
    listek = ["Atıklardan hediyelik eşya","Çöplerin hangi kutuya atılmasını söyleyen posterler","Atıkların ne kadar sürede doğada çözündüğünü gösteren tablo","Pillerin zararları","Kimyasal maddelerin kullanışı ve zararları"]
    rastgele = random.choice(listek)
    await ctx.send(rastgele)



bot.run(TOKEN)
