import discord
import logging
from discord.ext import commands
from typing import List
from tokens import GUILD_ID
from discord.commands.context import ApplicationContext
from views.sound_board_view import SoundBoard, VoiceClient
import os
import json

log = logging.getLogger(__name__)

SOUND_CONFIG_FILE = "./sounds/sounds_config.json"
ALLOWED_CONTENT_TYPES = ["audio/mpeg"]
SOUNDS_PER_BOARD = 25


class SoundBoardCog(commands.Cog):
    command_group = discord.SlashCommandGroup(
        "soundboard", "A group of commands to use the soundboard"
    )

    def __init__(self, bot) -> None:
        self.bot: discord.Bot = bot
        self._sounds = self._load_sounds()
        self.vc = VoiceClient()

    def _load_sounds(self):
        if not os.path.exists(SOUND_CONFIG_FILE):
            return {}

        with open(SOUND_CONFIG_FILE) as file:
            sounds = json.load(file)

        return sounds

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: discord.Member,
        before: discord.VoiceState,
        after: discord.VoiceState,
    ):
        channel = before.channel or after.channel
        should_leave = True
        for member in channel.members:
            should_leave &= member.bot

        if should_leave:
            for client in self.bot.voice_clients:
                await client.disconnect()

    @command_group.command(
        name="open",
        description="opens the soundboard",
        guild=discord.Object(id=GUILD_ID),
    )
    async def open_soundboard(self, context: ApplicationContext):
        if not self._sounds:
            await context.response.send_message("No sounds configured")
            return

        num_boards = len(self._sounds) // SOUNDS_PER_BOARD
        num_boards += 1 if len(self._sounds) % SOUNDS_PER_BOARD > 0 else 0
        boards: List[SoundBoard] = []
        for i in range(num_boards):
            first = SOUNDS_PER_BOARD * i
            last = SOUNDS_PER_BOARD * i + SOUNDS_PER_BOARD
            sound_group = dict(list(self._sounds.items())[first:last])
            sound_board = SoundBoard(sound_group, self.bot, self.vc)
            boards.append(sound_board)

        for i, board in enumerate(boards):
            await board.send_board(context, first=i == 0)

    @command_group.command(
        name="add-sound",
        description="upload new sounds to the soundboard",
        guild=discord.Object(id=GUILD_ID),
    )
    @discord.option(name="name", description="The name u want to give the sound")
    @discord.option(name="file", description="The sound file")
    async def add_sound(
        self,
        context: ApplicationContext,
        name: str,
        file: discord.Attachment,
    ):
        if not context.author.guild_permissions.administrator:
            await context.response.send_message(
                "You are unauthorized to use this command. Please ask an admin to upload the sound"
            )
            return

        if os.path.exists(f"./sounds/{file.filename}"):
            await context.response.send_message(
                "Failed to upload sound.\nFile with the same filename already exists"
            )
            return

        if name in self._sounds.keys():
            await context.response.send_message(
                "Failed to upload sound.\nSound with the same name already exists"
            )
            return

        if file.content_type not in ALLOWED_CONTENT_TYPES:
            await context.response.send_message(
                "Failed to upload sound.\nFile content is not allowed (should be an audio file)"
            )
            return

        self._sounds[name] = file.filename
        self._save_sounds_config()

        await file.save(f"./sounds/{file.filename}")

        await context.response.send_message(
            f"Successfully uploaded sound: {name} | {file.filename}"
        )

    @command_group.command(
        name="remove-sound",
        description="upload new sounds to the soundboard",
        guild=discord.Object(id=GUILD_ID),
    )
    @discord.option(name="name", description="The name of the sound you want to delete")
    async def remove_sound(self, context: ApplicationContext, name: str):
        if not context.author.guild_permissions.administrator:
            await context.response.send_message(
                "You are unauthorized to use this command. Please ask an admin to upload the sound"
            )
            return

        if name not in self._sounds.keys():
            await context.response.send_message(
                "Cannot delete that sound since it does not exist"
            )
            return

        if os.path.exists(f"./sounds/{self._sounds[name]}"):
            os.remove(f"./sounds/{self._sounds[name]}")
        del self._sounds[name]
        self._save_sounds_config()
        await context.response.send_message(f"Succesfully deleted {name}")

    def _save_sounds_config(self):
        if not os.path.exists("./sounds"):
            os.mkdir("./sounds")

        with open(SOUND_CONFIG_FILE, "w") as config_file:
            json.dump(self._sounds, config_file)


def manual_setup(bot: discord.Bot) -> None:
    bot.add_cog(SoundBoardCog(bot))
    log.info("Finished setting up the soundboard cog")
