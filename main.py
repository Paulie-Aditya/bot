import nextcord
from nextcord.ext import commands


#Other files
import config_pauliebot

bot = commands.Bot(command_prefix= "!",intents=nextcord.Intents.all())



bot.run(config_pauliebot.bot_token)