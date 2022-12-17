

class AppMessage:
    """
    Message tempelete
    """
    ANSWER_FOR_BANNED_USERS = """
You have been banned, fuck off, please)
"""
    FORWARDED_MESSAGE = """
Message Infromation
First Name: {first_name}
Last Name: {last_name}
Username: @{username}
Phone Number: {phone_number}
IS My Contact: {is_contact}

<b>Message Text</b>
{text}
"""
    IS_NOT_CONTACT_USER = """
We don't have your contact, fuck off or send your contact!
"""


messages = AppMessage()
