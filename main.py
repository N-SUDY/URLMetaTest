from config import Config
from pyromod import listen
from pyrogram import Client, idle
from helper_fns.helper import clear_restart


User_Data = eval(Config.User_Data)

app = Client(
    "Nik66TestBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TOKEN,
    plugins=dict(root="bot"),
)


if __name__ == "__main__":
    app.start()
    if Config.USER:
            User = Config.USER.start()
            TGUserData = User.get_me()
            first_name = TGUserData.first_name
            if not TGUserData.is_premium:
                print(f"⛔User Account {first_name} Don't Have Telegram Premium, 2GB Limit Will Be Used For Telegram Uploading.")
            else:
                print(f"💎Telegram Premium Found For  User {first_name}")
            print(f'🔒User Session For {first_name} Started Successfully!🔒')
    uname = app.get_me().username
    try:
        if 'restart' in User_Data:
            if len(User_Data['restart'])!=0:
                datam = User_Data['restart'][0]
                app.run(clear_restart())
                print(datam)
                chat_id, msg_id = datam
                try:
                    app.edit_message_text(
                                                                        chat_id=chat_id,
                                                                        message_id=msg_id,
                                                                        text="✅Restarted Successfully"
                                                                    )
                except:
                    pass
    except Exception as e:
        print("🧩Error While Updating Restart Message:\n\n", e)
    print(f'✅@{uname} Started Successfully!✅')
    print(f"⚡Bot By Sahil Nolia⚡")
    idle()
    app.stop()
    print("💀Bot Stopped💀")
