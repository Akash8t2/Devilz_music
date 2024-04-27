import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AnonXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("AnonXMusic").info(
        b"\x00@\x00w\x00h\x00i\x00t\x00e\x00h\x00e\x00l\x00l\x000\x001\x001\x00 \x00'\x00s\x00 \x00M\x00u\x00s\x00i\x00c\x00 \x00B\x00o\x00t\x00 \x00S\x00t\x00a\x00r\x00t\x00e\x00d\x00 \x00S\x00u\x00c\x00c\x00e\x00s\x00s\x00f\x00u\x00l\x00l\x00y\x00.\x00\n\x00\n\x00D\x00o\x00n\x00'\x00t\x00 \x00f\x00o\x00r\x00g\x00e\x00t\x00 \x00t\x00o\x00 \x00v\x00i\x00s\x00i\x00t\x00 \x00@\x00d\x00i\x00l\x00_\x00k\x00i\x00_\x00b\x00a\x00a\x00t\x00e\x00e\x00 \x00a\x00n\x00d\x00 \x00@\x00h\x00e\x00a\x00r\x00t\x00_\x00t\x00a\x00l\x00k\x00z"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AnonXMusic").info("Stopping Devilz Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
