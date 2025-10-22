import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# -----------------------------
# COMANDOS BASE
# -----------------------------

@bot.event
async def on_ready():
    print('We have logged in as ' + str(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hola, soy un bot ' + str(bot.user) + '!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("$heh" * count_heh)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result) 

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

# -----------------------------
# DATOS ECOLOGICOS
# -----------------------------

datos_clasificacion = {
    "botella de plástico": {
        "info": "Reciclable (plástico PET). Lávalo y colócalo en el contenedor amarillo.",
        "video": "https://www.youtube.com/shorts/EXAMPLE1"
    },
    "papel": {
        "info": "Reciclable. Contenedor azul. Evita que se mezcle con comida o grasa.",
        "video": "https://www.youtube.com/shorts/EXAMPLE2"
    },
    "cáscara de fruta": {
        "info": "Residuo orgánico. Ideal para compostaje. Se convierte en abono natural.",
        "video": "https://www.youtube.com/shorts/EXAMPLE3"
    },
    "lata": {
        "info": "Reciclable (metal). Contenedor amarillo. El aluminio puede reciclarse infinitamente.",
        "video": "https://www.youtube.com/shorts/EXAMPLE4"
    },
    "vidrio": {
        "info": "Reciclable. Contenedor verde. No mezcles vidrios rotos con otros materiales.",
        "video": "https://www.youtube.com/shorts/EXAMPLE5"
    }
}

datos_descomposicion = {
    "botella de plástico": {
        "info": "450 a 500 años. Contamina océanos y tarda siglos en degradarse.",
        "video": "https://www.youtube.com/shorts/EXAMPLE6"
    },
    "lata": {
        "info": "200 a 500 años. El aluminio tarda mucho pero se puede reciclar fácilmente.",
        "video": "https://www.youtube.com/shorts/EXAMPLE7"
    },
    "vidrio": {
        "info": "Más de 4000 años. Es prácticamente eterno si no se recicla.",
        "video": "https://www.youtube.com/shorts/EXAMPLE8"
    },
    "papel": {
        "info": "2 a 5 meses. Se degrada rápido, pero reciclarlo ahorra muchos árboles.",
        "video": "https://www.youtube.com/shorts/EXAMPLE9"
    }
}

datos_ideas = {
    "plástico": [
        {
            "texto": "Haz una maceta cortando una botella por la mitad y decorándola.",
            "video": "https://www.youtube.com/shorts/VIDEO1"
        },
        {
            "texto": "Crea un comedero para pájaros con una botella y cucharas.",
            "video": "https://www.youtube.com/shorts/VIDEO2"
        }
    ],
    "cartón": [
        {
            "texto": "Haz una casa para gatos o una caja organizadora.",
            "video": "https://www.youtube.com/shorts/VIDEO3"
        },
        {
            "texto": "Construye un soporte para celular con cartón reciclado.",
            "video": "https://www.youtube.com/shorts/VIDEO4"
        }
    ],
    "vidrio": [
        {
            "texto": "Usa frascos de vidrio como lámparas decorativas.",
            "video": "https://www.youtube.com/shorts/VIDEO5"
        },
        {
            "texto": "Haz velas dentro de frascos pequeños.",
            "video": "https://www.youtube.com/shorts/VIDEO6"
        }
    ]
}

datos_tips = [
    {
        "texto": "Apaga las luces cuando no las necesites.",
        "video": "https://www.youtube.com/shorts/VIDEO7"
    },
    {
        "texto": "Usa bolsas reutilizables en vez de plásticas.",
        "video": "https://www.youtube.com/shorts/VIDEO8"
    },
    {
        "texto": "Cierra el grifo mientras te cepillas los dientes.",
        "video": "https://www.youtube.com/shorts/VIDEO9"
    },
    {
        "texto": "Recicla siempre papel, plástico y vidrio.",
        "video": "https://www.youtube.com/shorts/VIDEO10"
    },
    {
        "texto": "No tires basura en la calle o ríos.",
        "video": "https://www.youtube.com/shorts/VIDEO11"
    },
    {
        "texto": "Reduce el consumo de botellas plásticas de un solo uso.",
        "video": "https://www.youtube.com/shorts/VIDEO12"
    },
    {
        "texto": "Prefiere transporte público o bicicleta para cuidar el medio ambiente.",
        "video": "https://www.youtube.com/shorts/VIDEO13"
    },
    {
        "texto": "Reutiliza cajas y frascos para almacenamiento.",
        "video": "https://www.youtube.com/shorts/VIDEO14"
    }
]

datos_curiosos = [
    {
        "texto": "El 80% de la basura en el mar es plástico.",
        "video": "https://www.youtube.com/shorts/VIDEO15"
    },
    {
        "texto": "Cada tonelada de papel reciclado salva 17 árboles.",
        "video": "https://www.youtube.com/shorts/VIDEO16"
    },
    {
        "texto": "Se estima que en 2050 habrá más plástico que peces en el océano.",
        "video": "https://www.youtube.com/shorts/VIDEO17"
    },
    {
        "texto": "Reciclar 1 botella de vidrio ahorra suficiente energía para encender una bombilla durante 4 horas.",
        "video": "https://www.youtube.com/shorts/VIDEO18"
    },
    {
        "texto": "El reciclaje de aluminio puede hacerse infinitas veces sin perder calidad.",
        "video": "https://www.youtube.com/shorts/VIDEO19"
    },
    {
        "texto": "Un millón de botellas plásticas se compran cada minuto en el mundo.",
        "video": "https://www.youtube.com/shorts/VIDEO20"
    },
    {
        "texto": "Reducir, reutilizar y reciclar es la regla de oro del cuidado ambiental.",
        "video": "https://www.youtube.com/shorts/VIDEO21"
    }
]

# -----------------------------
# COMANDOS ECOGUARDIAN
# -----------------------------

@bot.command()
async def clasificar(ctx, *, objeto: str):
    objeto = objeto.lower()
    if objeto in datos_clasificacion:
        data = datos_clasificacion[objeto]
        await ctx.send(data["info"])
        await ctx.send(data["video"])
    else:
        await ctx.send("No tengo información sobre ese objeto.")

@bot.command()
async def descomposicion(ctx, *, objeto: str):
    objeto = objeto.lower()
    if objeto in datos_descomposicion:
        data = datos_descomposicion[objeto]
        await ctx.send(data["info"])
        await ctx.send(data["video"])
    else:
        await ctx.send("No tengo datos sobre ese objeto.")

@bot.command()
async def idea(ctx, *, material: str):
    material = material.lower()
    if material in datos_ideas:
        seleccion = random.choice(datos_ideas[material])
        await ctx.send(seleccion["texto"])
        await ctx.send(seleccion["video"])
    else:
        await ctx.send("No tengo ideas con ese material todavía.")

@bot.command()
async def tip(ctx):
    seleccion = random.sample(datos_tips, k=min(7, len(datos_tips)))
    for t in seleccion:
        await ctx.send(t["texto"])
        await ctx.send(t["video"])

@bot.command()
async def dato(ctx):
    seleccion = random.sample(datos_curiosos, k=min(7, len(datos_curiosos)))
    for d in seleccion:
        await ctx.send(d["texto"])
        await ctx.send(d["video"])

@bot.command()
async def ayuda(ctx):
    mensaje = ""
    mensaje += "$clasificar [objeto] → Te dice si se recicla y muestra un video.\n"
    mensaje += "$descomposicion [objeto] → Muestra cuánto tarda en degradarse y un video.\n"
    mensaje += "$idea [material] → Te da una idea ecológica con video.\n"
    mensaje += "$tip → Te da 7 consejos ecológicos con video.\n"
    mensaje += "$dato → Te da 7 datos curiosos con video.\n"
    mensaje += "$hello, $heh, $roll, $bot → comandos base del bot.\n"
    await ctx.send(mensaje)

# -----------------------------
# EJECUCIÓN DEL BOT
# -----------------------------
