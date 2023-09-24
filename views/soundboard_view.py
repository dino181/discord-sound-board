import discord
import logging

import discord
from discord.commands.context import ApplicationContext
from discord.channel import DMChannel, TextChannel
from typing import Union
import embed_messages.soundboard_messages as messages
from tokens import BASE_PATH

log = logging.getLogger(__name__)


class VoiceClient:
    def __init__(self):
        self.vc: discord.VoiceClient = None


class SoundBoard(discord.ui.View):
    def __init__(self, sounds: dict[str, str], bot, vc: VoiceClient) -> None:
        super().__init__(timeout=None)
        self._sounds = sounds
        self.message = None
        self.bot: discord.Bot = bot
        self._callbacks = {
            0: self._play_sound_0,
            1: self._play_sound_1,
            2: self._play_sound_2,
            3: self._play_sound_3,
            4: self._play_sound_4,
            5: self._play_sound_5,
            6: self._play_sound_6,
            7: self._play_sound_7,
            8: self._play_sound_8,
            9: self._play_sound_9,
            10: self._play_sound_10,
            11: self._play_sound_11,
            12: self._play_sound_12,
            13: self._play_sound_13,
            14: self._play_sound_14,
            15: self._play_sound_15,
            16: self._play_sound_16,
            17: self._play_sound_17,
            18: self._play_sound_18,
            19: self._play_sound_19,
            20: self._play_sound_20,
            21: self._play_sound_21,
            22: self._play_sound_22,
            23: self._play_sound_23,
            24: self._play_sound_24,
        }
        self._voice_client: VoiceClient = vc

    async def send_board(
        self,
        context: Union[ApplicationContext, DMChannel, TextChannel],
        first: bool = False,
    ) -> None:
        """
        Sends the first page of the multipage
        """
        self._create_board()
        if first:
            embed = messages.soundboard_header()
            await context.response.send_message(embed=embed, view=self)

        else:
            await context.send(view=self)

    def _create_board(self):
        for i, name in enumerate(self._sounds.keys()):
            btn = discord.ui.Button(
                label=name, style=discord.ButtonStyle.success, disabled=False
            )
            btn.callback = self._callbacks[i]
            self.add_item(btn)

    async def _join_voice_channel(self, interaction: discord.Interaction):
        user: discord.User | discord.Member = interaction.user
        voice: discord.VoiceState = user.voice
        log.critical(f"vc: {self._voice_client.vc}")
        if voice and not self._voice_client.vc:
            voice_channel = voice.channel
            self._voice_client.vc = await voice_channel.connect()

        elif voice and voice.channel != self._voice_client.vc.channel:
            await self._voice_client.vc.disconnect()
            voice_channel = voice.channel
            self._voice_client.vc = await voice_channel.connect()

    async def _play_sound(self, sound: str):
        if self._voice_client.vc:
            self._voice_client.vc.stop()
            sound = discord.FFmpegPCMAudio(
                f"{BASE_PATH}/sounds/{sound}", executable="./ffmpeg/bin/ffmpeg.exe"
            )
            self._voice_client.vc.play(sound)

    async def _play_sound_0(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[0]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_1(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[1]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_2(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[2]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_3(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[3]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_4(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[4]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_5(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[5]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_6(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[6]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_7(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[7]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_8(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[8]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_9(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[9]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_10(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[10]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_11(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[11]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_12(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[12]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_13(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[13]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_14(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[14]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_15(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[15]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_16(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[16]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_17(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[17]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_18(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[18]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_19(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[19]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_20(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[20]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_21(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[21]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_22(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[22]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_23(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[23]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)

    async def _play_sound_24(self, interaction: discord.Interaction):
        sound_location = list(self._sounds.values())[24]
        await self._join_voice_channel(interaction)
        await self._play_sound(sound_location)
        await interaction.response.edit_message(view=self)
