from discord import Embed

RED = 0xCF0A0A
GREEN = 0x0ACF0A
BLUE = 0x2ED7E3


def error_message(text: str):
    embed = Embed(
        title=":x: Failed to perform command",
        description=f"`reason`: {text}",
        color=RED,
    )
    return embed


def uploaded_sound(name: str, file: str):
    embed = Embed(
        title=":white_check_mark: Uploaded sound",
        description="use `/soundboard open` to access the new sound",
        color=GREEN,
    )
    embed.add_field(name="sound name", value=f"`{name}`", inline=False)
    embed.add_field(name="sound file", value=f"`{file}`", inline=False)

    return embed


def deleted_sound(name):
    embed = Embed(title=":white_check_mark: Deleted sound", color=GREEN)
    embed.add_field(name="sound name", value=name)
    return embed


def soundboard_header():
    embed = Embed(title="--==| Totally a legit Sound board |==--", color=BLUE)
    return embed
