from pyrogram.handlers import MessageHandler

from libraries.client import app
from handlers.delete_handler import delete_handler


# delete handler
app.add_handler(
    handler=MessageHandler(
        callback=delete_handler
    )
)

app.run()
