from app import bot
def checkmember(user_id):
    try:
        member=bot.get_chat_member('@Behzod_Asliddinov',user_id).status
        if (member=='member') or (member=='creator') or (member=='madminstrator'):
            return True
    except    :
        return False