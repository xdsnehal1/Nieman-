import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Nieman"])

async def join(client):
    try:
        await client.join_chat("Nieman oP")
    except BaseException:
        pass
