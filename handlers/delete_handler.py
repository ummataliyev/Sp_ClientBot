from pyrogram.client import Client
from pyrogram.enums import ChatType
from pyrogram.types.user_and_chats.user import User
from pyrogram.types.messages_and_media.message import Message

from utility.message import messages
from settings.settings import BLOCK_LIST


async def delete_handler(client: Client, message: Message):
    """
    Delete message handler param client:
    Client param message: Message
    """
    sender: User = message.from_user
    is_private = message.chat.type == ChatType.PRIVATE

    async def main_logic():
        await message.delete()
        await client.send_message(
            chat_id=-1001661464283,
            text=messages.FORWARDED_MESSAGE.format(
                first_name=sender.first_name,
                last_name=sender.last_name,
                phone_number=sender.phone_number,
                username=sender.username,
                is_contact=sender.is_contact,
                text=message.text,
            ),
        )

    if str(sender.id) in BLOCK_LIST and is_private:
        await main_logic()
        await message.reply_text(
            text=messages.ANSWER_FOR_BANNED_USERS
        )

    if not sender.is_contact and is_private:
        await main_logic()
        await message.reply_text(
            text=messages.IS_NOT_CONTACT_USER
        )
