import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def help(ctx):
    help_text = """
    **Comandos disponibles:**

    **$hello** - Saluda al bot.
    **$heh [count]** - Envía una cadena de "he" repetida la cantidad que determines (por defecto es 5).
    **$add [numero1] [numero2]** - Suma dos números.
    **$cool [nombre]** - Dice si un usuario es "cool".
    """
    await ctx.send(help_text)
            
bot.run("")
