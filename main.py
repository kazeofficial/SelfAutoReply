from telethon import TelegramClient, events

api_id = 32890317
api_hash = "60ec62cec829ba29c99809a12e0dc494"

client = TelegramClient("session", api_id, api_hash)

AUTO_REPLY = """
👋 Hi!

Offline ako ngayon.
Magrereply ako kapag available na.

Salamat!
"""

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:
        await event.reply(AUTO_REPLY)

client.start()
client.run_until_disconnected()
