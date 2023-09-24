import discord
import logging

from tokens import GUILD_ID, BOT_TOKEN
from logger.logger import setup_logger

import cogs.soundboard as sound_board_cog

setup_logger()

log = logging.getLogger(__name__)

bot = discord.Bot(debug_guilds=[GUILD_ID], intents=discord.Intents.all())
bot.allowed_mentions = discord.AllowedMentions(everyone=True)


@bot.event
async def on_ready():
    await bot.sync_commands()
    log.info("We have logged in as {0.user}".format(bot))


if __name__ == "__main__":
    sound_board_cog.manual_setup(bot)

    bot.run(BOT_TOKEN)
