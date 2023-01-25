from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from helper_fns.helper import USER_DATA, saveconfig, check_filex, delete_all, delete_trash,saveoptions
from os import listdir
from os.path import isfile, exists




############Variables##############
sudo_users = eval(Config.SUDO_USERS)
wpositions = {'5:5': 'Top Left', 'main_w-overlay_w-5:5': 'Top Right', '5:main_h-overlay_h': 'Bottom Left', 'main_w-overlay_w-5:main_h-overlay_h-5': 'Bottom Right'}




############CallBack##############
@Client.on_callback_query()
async def newbt(client, callback_query):
        txt = callback_query.data
        user_id = callback_query.message.chat.id
        userx = callback_query.from_user.id
        print(txt)
        # await callback_query.message.delete()
        
        
        if txt.startswith("position_") or txt.startswith("cname_") or txt.startswith("cmdata_") or txt.startswith("size_") or txt.startswith("wpreset_") or txt.startswith("mpreset_") or txt.startswith("cpreset_") or txt.startswith("ccrp_") or txt.startswith("sstream_") or txt.startswith("autostream_") or txt.startswith("splitvideo_") or txt.startswith("splitsize_") or txt.startswith("uploadtg_") or txt.startswith("setrclone_") or txt.startswith("cthumb_"):
                new_position = txt.split("_", 1)[1]
                if txt.startswith("position_"):
                    await saveconfig(userx, 'watermark', 'position', new_position)
                elif txt.startswith("size_"):
                    await saveconfig(userx, 'watermark', 'size', new_position)
                elif txt.startswith("wpreset_"):
                    await saveconfig(userx, 'watermark', 'preset', new_position)
                elif txt.startswith("mpreset_"):
                    await saveconfig(userx, 'muxer', 'preset', new_position)
                elif txt.startswith("cpreset_"):
                    await saveconfig(userx, 'compress', 'preset', new_position)
                elif txt.startswith("sstream_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'select_stream', new_position)
                elif txt.startswith("autostream_"):
                    await saveoptions(userx, 'stream', new_position)
                elif txt.startswith("splitvideo_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'split_video', new_position)
                elif txt.startswith("splitsize_"):
                    await saveoptions(userx, 'split', new_position)
                elif txt.startswith("uploadtg_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'upload_tg', new_position)
                elif txt.startswith("cname_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'custom_name', new_position)
                elif txt.startswith("cmdata_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'custom_metadata', new_position)
                elif txt.startswith("setrclone_"):
                    await saveoptions(userx, 'drive_name', new_position)
                elif txt.startswith("cthumb_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveoptions(userx, 'custom_thumbnail', new_position)
                watermark_position = USER_DATA()[userx]['watermark']['position']
                watermark_size = USER_DATA()[userx]['watermark']['size']
                watermark_preset = USER_DATA()[userx]['watermark']['preset']
                muxer_preset = USER_DATA()[userx]['muxer']['preset']
                compress_preset = USER_DATA()[userx]['compress']['preset']
                select_stream = USER_DATA()[userx]['select_stream']
                stream = USER_DATA()[userx]['stream']
                split_video = USER_DATA()[userx]['split_video']
                split = USER_DATA()[userx]['split']
                upload_tg = USER_DATA()[userx]['upload_tg']
                rclone = USER_DATA()[userx]['rclone']
                custom_metadata = USER_DATA()[userx]['custom_metadata']
                custom_thumbnail = USER_DATA()[userx]['custom_thumbnail']
                drive_name = USER_DATA()[userx]['drive_name']
                custom_name = USER_DATA()[userx]['custom_name']
                positions = {'Set Top Left':"position_5:5", "Set Top Right": "position_main_w-overlay_w-5:5", "Set Bottom Left": "position_5:main_h-overlay_h", "Set Bottom Right": "position_main_w-overlay_w-5:main_h-overlay_h-5"}
                sizes = [5,7,10,13,15,17,20,25,30,35,40,45]
                pkeys = list(positions.keys())
                KeyBoard = []
                KeyBoard.append([InlineKeyboardButton(f"🔶Watermark Position - {wpositions[watermark_position]}🔶", callback_data="lol-wposition")])
                WP1 = []
                WP2 = []
                zx = 1
                for z in pkeys:
                    s_position = positions[z].replace('position_', '')
                    if s_position !=watermark_position:
                            datam = z
                    else:
                        datam = f"{str(z)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=str(positions[z]))
                    if zx<3:
                        WP1.append(keyboard)
                    else:
                        WP2.append(keyboard)
                    zx+=1
                KeyBoard.append(WP1)
                KeyBoard.append(WP2)
                KeyBoard.append([InlineKeyboardButton(f"🔶Watermark Size - {str(watermark_size)}%🔶", callback_data="lol-wsize")])
                WS1 = []
                WS2 = []
                WS3 = []
                zz = 1
                for x in sizes:
                    vlue = f"size_{str(x)}"
                    if int(watermark_size)!=int(x):
                        datam = f"{str(x)}%"
                    else:
                        datam = f"{str(x)}% 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    if zz<5:
                            WS1.append(keyboard)
                    elif zz<9:
                            WS2.append(keyboard)
                    else:
                            WS3.append(keyboard)
                    zz+=1
                KeyBoard.append(WS1)
                KeyBoard.append(WS2)
                KeyBoard.append(WS3)
                KeyBoard.append([InlineKeyboardButton(f"🔶Watermark Preset - {watermark_preset}🔶", callback_data="lol-wpset")])
                presets = ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']
                WX1 = []
                WX2 = []
                WX3 = []
                zz = 1
                for pp in presets:
                    if watermark_preset!=pp:
                        datam = pp
                    else:
                        datam = f"{str(pp)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=f'wpreset_{str(pp)}')
                    if zz<4:
                            WX1.append(keyboard)
                    elif zz<7:
                            WX2.append(keyboard)
                    else:
                            WX3.append(keyboard)
                    zz+=1
                KeyBoard.append(WX1)
                KeyBoard.append(WX2)
                KeyBoard.append(WX3)
                KeyBoard.append([InlineKeyboardButton(f"🔶Muxer Preset - {muxer_preset}🔶", callback_data="lol-mpset")])
                MP1 = []
                MP2 = []
                MP3 = []
                zz = 1
                for pp in presets:
                    if muxer_preset!=pp:
                        datam = pp
                    else:
                        datam = f"{str(pp)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=f'mpreset_{str(pp)}')
                    if zz<4:
                            MP1.append(keyboard)
                    elif zz<7:
                            MP2.append(keyboard)
                    else:
                            MP3.append(keyboard)
                    zz+=1
                KeyBoard.append(MP1)
                KeyBoard.append(MP2)
                KeyBoard.append(MP3)
                KeyBoard.append([InlineKeyboardButton(f"🔶Compress Preset - {compress_preset}🔶", callback_data="lol-cpset")])
                cp1 = []
                cp2 = []
                cp3 = []
                zz = 1
                for pp in presets:
                    if compress_preset!=pp:
                        datam = pp
                    else:
                        datam = f"{str(pp)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=f'cpreset_{str(pp)}')
                    if zz<4:
                            cp1.append(keyboard)
                    elif zz<7:
                            cp2.append(keyboard)
                    else:
                            cp3.append(keyboard)
                    zz+=1
                KeyBoard.append(cp1)
                KeyBoard.append(cp2)
                KeyBoard.append(cp3)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Select Stream - {str(select_stream)}🔶", callback_data="lol-sstream")])
                st = []
                for x in streams:
                    vlue = f"sstream_{str(x)}"
                    if select_stream!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['ENG', 'HIN']
                KeyBoard.append([InlineKeyboardButton(f"🔶Auto Select Stream - {str(stream)}🔶", callback_data="lol-sstream")])
                st = []
                for x in streams:
                    vlue = f"autostream_{str(x)}"
                    if stream!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Split Video - {str(split_video)}🔶", callback_data="lol-splitv")])
                st = []
                for x in streams:
                    vlue = f"splitvideo_{str(x)}"
                    if split_video!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['2GB', '4GB']
                KeyBoard.append([InlineKeyboardButton(f"🔶Split Size - {str(split)}🔶", callback_data="lol-splits")])
                st = []
                for x in streams:
                    vlue = f"splitsize_{str(x)}"
                    if split!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Upload On TG - {str(upload_tg)}🔶", callback_data="lol-sp")])
                st = []
                for x in streams:
                    vlue = f"uploadtg_{str(x)}"
                    if upload_tg!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Use Custom Thumb - {str(custom_thumbnail)}🔶", callback_data="lol-custv")])
                st = []
                for x in streams:
                    vlue = f"cthumb_{str(x)}"
                    if custom_thumbnail!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Use Custom Name - {str(custom_name)}🔶", callback_data="lol-custn")])
                st = []
                for x in streams:
                    vlue = f"cname_{str(x)}"
                    if custom_name!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🔶Change MetaData- {str(custom_metadata)}🔶", callback_data="lol-custn")])
                st = []
                for x in streams:
                    vlue = f"cmdata_{str(x)}"
                    if custom_metadata!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                r_config = f'./userdata/{str(userx)}_rclone.conf'
                if not exists(r_config):
                        KeyBoard.append([InlineKeyboardButton(f"🔶Rclone Config Not Found🔶", callback_data="lol-rclonenotfound")])
                else:
                                try:
                                        with open(r_config) as f:
                                                rdata = f.readlines()
                                        accounts = []
                                        for line in rdata:
                                                        line = line.strip()
                                                        if line.startswith('[') and line.endswith(']'):
                                                                accounts.append(line.replace('[', '').replace(']', ''))
                                        st = []
                                        if len(accounts)!=0:
                                                for x in accounts:
                                                        vlue = f"setrclone_{str(x)}"
                                                        if drive_name!=x:
                                                                datam = f"{str(x)}"
                                                        else:
                                                                datam = f"{str(x)} 🟢"
                                                        keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                                                        st.append(keyboard)
                                                KeyBoard.append([InlineKeyboardButton(f"🔶Current Rclone Account - {str(drive_name)}🔶", callback_data="lol-sp")])
                                                KeyBoard.append(st)
                                except Exception as e:
                                        await client.send_message(user_id, f"❗Error While Getting Rclone Accounts\n\nError: {str(e)}")
                try:
                    await callback_query.message.edit(
                        text="Settings",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(KeyBoard))
                except Exception as e:
                    print(e)
                return
            

        elif txt.startswith("encoderw_") or txt.startswith("encodew_") or txt.startswith("encoderm_") or txt.startswith("encodem_") or txt.startswith("encoderc_"):
                new_position = txt.split("_", 1)[1]
                if txt.startswith("encodew_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'watermark', 'encode', new_position)
                elif txt.startswith("encoderw_"):
                    await saveconfig(userx, 'watermark', 'encoder', new_position)
                elif txt.startswith("encodem_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'muxer', 'encode', new_position)
                elif txt.startswith("encoderm_"):
                    await saveconfig(userx, 'muxer', 'encoder', new_position)
                elif txt.startswith("encoderc_"):
                    await saveconfig(userx, 'compress', 'encoder', new_position)
                encode_watermark = USER_DATA()[userx]['watermark']['encode']
                encode_muxer = USER_DATA()[userx]['muxer']['encode']
                watermark_encoder = USER_DATA()[userx]['watermark']['encoder']
                muxer_encoder = USER_DATA()[userx]['muxer']['encoder']
                compress_encoder = USER_DATA()[userx]['compress']['encoder']
                KeyBoard = []
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🛺Encode WaterMark Video - {str(encode_watermark)}🛺", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encodew_{str(x)}"
                    if encode_watermark!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['libx265', 'libx264']
                KeyBoard.append([InlineKeyboardButton(f"🔶WaterMark Encoder - {str(watermark_encoder)}🔶", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encoderw_{str(x)}"
                    if watermark_encoder!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🎮Encode Muxer Video - {str(encode_muxer)}🎮", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encodem_{str(x)}"
                    if encode_muxer!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['libx265', 'libx264']
                KeyBoard.append([InlineKeyboardButton(f"🔶Muxer Encoder - {str(muxer_encoder)}🔶", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encoderm_{str(x)}"
                    if muxer_encoder!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['libx265', 'libx264']
                KeyBoard.append([InlineKeyboardButton(f"🏮Compress Encoder - {str(compress_encoder)}🏮", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encoderc_{str(x)}"
                    if compress_encoder!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                try:
                    await callback_query.message.edit(
                        text="Settings",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(KeyBoard))
                except Exception as e:
                    print(e)
                return
                    
    
        elif txt.startswith("ccrf_") or txt.startswith("wcrf_") or txt.startswith("mcrf_") or txt.startswith("usecw_") or txt.startswith("usecm_"):
                new_position = txt.split("_", 1)[1]
                if txt.startswith("ccrf_"):
                        await saveconfig(userx, 'compress', 'crf', new_position)
                elif txt.startswith("wcrf_"):
                        await saveconfig(userx, 'watermark', 'crf', new_position)
                elif txt.startswith("mcrf_"):
                        await saveconfig(userx, 'muxer', 'crf', new_position)
                elif txt.startswith("usecm_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'muxer', 'use_crf', new_position)
                elif txt.startswith("usecw_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'watermark', 'use_crf', new_position)
                compress_crf = USER_DATA()[userx]['compress']['crf']
                watermark_crf = USER_DATA()[userx]['watermark']['crf']
                muxer_crf = USER_DATA()[userx]['muxer']['crf']
                use_crf_watermark = USER_DATA()[userx]['watermark']['use_crf']
                use_crf_muxer = USER_DATA()[userx]['muxer']['use_crf']
                crfs = [0, 3, 6, 9, 12, 15, 18, 21, 23, 24, 27, 28, 30, 33, 36, 39, 42, 45, 48, 51]
                KeyBoard = []
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🛺Use WaterMark CRF - {str(use_crf_watermark)}🛺", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"usecw_{str(x)}"
                    if use_crf_watermark!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                KeyBoard.append([InlineKeyboardButton(f"🔶WaterMark CRF - {watermark_crf}🔶", callback_data="lol-wcrf")])
                CCRP1 = []
                CCRP2 = []
                CCRP3 = []
                CCRP4 = []
                CCRP5 = []
                zz = 1
                for x in crfs:
                    vlue = f"wcrf_{str(x)}"
                    if int(watermark_crf)!=int(x):
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    if zz<5:
                            CCRP1.append(keyboard)
                    elif zz<9:
                            CCRP2.append(keyboard)
                    elif zz<13:
                            CCRP3.append(keyboard)
                    elif zz<17:
                        CCRP4.append(keyboard)
                    else:
                        CCRP5.append(keyboard)
                    zz+=1
                KeyBoard.append(CCRP1)
                KeyBoard.append(CCRP2)
                KeyBoard.append(CCRP3)
                KeyBoard.append(CCRP4)
                KeyBoard.append(CCRP5)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🎮Use Muxer CRF - {str(use_crf_muxer)}🎮", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"usecm_{str(x)}"
                    if use_crf_muxer !=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                KeyBoard.append([InlineKeyboardButton(f"🔶Muxer CRF - {muxer_crf}🔶", callback_data="lol-mcrf")])
                CCRP1 = []
                CCRP2 = []
                CCRP3 = []
                CCRP4 = []
                CCRP5 = []
                zz = 1
                for x in crfs:
                    vlue = f"mcrf_{str(x)}"
                    if int(muxer_crf)!=int(x):
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    if zz<5:
                            CCRP1.append(keyboard)
                    elif zz<9:
                            CCRP2.append(keyboard)
                    elif zz<13:
                            CCRP3.append(keyboard)
                    elif zz<17:
                        CCRP4.append(keyboard)
                    else:
                        CCRP5.append(keyboard)
                    zz+=1
                KeyBoard.append(CCRP1)
                KeyBoard.append(CCRP2)
                KeyBoard.append(CCRP3)
                KeyBoard.append(CCRP4)
                KeyBoard.append(CCRP5)
                KeyBoard.append([InlineKeyboardButton(f"🔶Compress CRF - {compress_crf}🔶", callback_data="lol-ccrp")])
                CCRP1 = []
                CCRP2 = []
                CCRP3 = []
                CCRP4 = []
                CCRP5 = []
                zz = 1
                for x in crfs:
                    vlue = f"ccrf_{str(x)}"
                    if int(compress_crf)!=int(x):
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    if zz<5:
                            CCRP1.append(keyboard)
                    elif zz<9:
                            CCRP2.append(keyboard)
                    elif zz<13:
                            CCRP3.append(keyboard)
                    elif zz<17:
                        CCRP4.append(keyboard)
                    else:
                        CCRP5.append(keyboard)
                    zz+=1
                KeyBoard.append(CCRP1)
                KeyBoard.append(CCRP2)
                KeyBoard.append(CCRP3)
                KeyBoard.append(CCRP4)
                KeyBoard.append(CCRP5)
                try:
                    await callback_query.message.edit(
                        text="Settings",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(KeyBoard))
                except Exception as e:
                    print(e)
                return


        elif txt.startswith("lol"):
            data = txt.split('-')
            keyx = data[1]
            if keyx=='water':
                watermark_path = f'./{str(userx)}_watermark.jpg'
                try:
                    await client.send_document(chat_id=user_id, document=watermark_path, caption=f"Nik66Bots")
                except:
                    await callback_query.answer(
                                f'⚡Nik66Bots⚡',
                                show_alert=True
                            )
            else:
                await callback_query.answer(
                                f'⚡Nik66Bots⚡',
                                show_alert=True
                            )
            return
        elif txt == "renewme":
            await callback_query.message.delete()
            g_d_list = ['db_handler.py', 'config.py', 'bot', 'requirements.txt', 'Dockerfile', 'config.env', 'helper_fns', 'docker-compose.yml', 'thumb.jpg', 'main.py', 'userdata']
            g_list = listdir()
            g_del_list = list(set(g_list) - set(g_d_list))
            deleted = []
            if len(g_del_list) != 0:
                for f in g_del_list:
                    if isfile(f):
                        if not(f.endswith(".session")) and not(f.endswith(".session-journal")):
                            print(f)
                            await delete_trash(f)
                            deleted.append(f)
                    else:
                        print(f)
                        await delete_all(f)
                        deleted.append(f)
                text = f"✔Deleted {len(deleted)} objects 🚮\n\n{str(deleted)}"
                try:
                        await callback_query.answer(
                                text,
                                show_alert=True)
                except:
                    await client.send_message(chat_id=user_id,
                            text=text)
                    
            else:
                await callback_query.answer(
                        f"Nothing to clear 🙄",
                        show_alert=True)
            return
        
        elif txt.startswith("notdelete"):
            await callback_query.answer(
                        f"Ok Dont Waste My Time😂",
                        show_alert=True)
            return
        

        elif txt.startswith("cmapsub_") or txt.startswith("mrgmap_"):
                new_position = txt.split("_", 1)[1]
                if txt.startswith("cmapsub_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'compress', 'map_sub', new_position)
                elif txt.startswith("mrgmap_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'merge', 'map', new_position)
                compress_sub_map = USER_DATA()[userx]['compress']['map_sub']
                merge_map = USER_DATA()[userx]['merge']['map']
                KeyBoard = []
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🏮Copy Compress Subtitles - {str(compress_sub_map)}🏮", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"cmapsub_{str(x)}"
                    if compress_sub_map!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🍧Map Merged Streams - {str(merge_map)}🍧", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"mrgmap_{str(x)}"
                    if merge_map!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                try:
                    await callback_query.message.edit(
                        text="Settings",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(KeyBoard))
                except Exception as e:
                    print(e)
                return
            
            

        elif txt.startswith("convert_") or txt.startswith("cquality_") or txt.startswith("cnvpreset_") or txt.startswith("usecnvcrf_") or txt.startswith("cnvcrf_") or txt.startswith("cnvsmap_") or txt.startswith("encodecnv_") or txt.startswith("encodercnv_"):
                new_position = txt.split("_", 1)[1]
                if txt.startswith("convert_"):
                    await saveoptions(userx, 'convert_video', eval(new_position))
                elif txt.startswith("cquality_"):
                    await saveoptions(userx, 'convert_quality', eval(new_position))
                elif txt.startswith("cnvpreset_"):
                    await saveconfig(userx, 'convert', 'preset', new_position)
                elif txt.startswith("usecnvcrf_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'convert', 'use_crf', new_position)
                elif txt.startswith("cnvcrf_"):
                        await saveconfig(userx, 'convert', 'crf', new_position)
                elif txt.startswith("cnvsmap_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'convert', 'map', new_position)
                elif txt.startswith("encodecnv_"):
                    if new_position=="True":
                        new_position = True
                    else:
                        new_position = False
                    await saveconfig(userx, 'convert', 'encode', new_position)
                elif txt.startswith("encodercnv_"):
                        await saveconfig(userx, 'convert', 'encoder', new_position)
                convert_video = USER_DATA()[userx]['convert_video']
                convert_quality = USER_DATA()[userx]['convert_quality']
                convert_preset = USER_DATA()[userx]['convert']['preset']
                convert_crf = USER_DATA()[userx]['convert']['crf']
                use_crf_convert = USER_DATA()[userx]['convert']['use_crf']
                convert_map = USER_DATA()[userx]['convert']['map']
                encode_convert = USER_DATA()[userx]['convert']['encode']
                convert_encoder = USER_DATA()[userx]['convert']['encoder']
                KeyBoard = []
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🌸Convert Video - {str(convert_video)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"convert_{str(x)}"
                    if convert_video!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [[720, 480],[720], [480]]
                KeyBoard.append([InlineKeyboardButton(f"🌸Convert Qualities - {str(convert_quality)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"cquality_{str(x)}"
                    if convert_quality!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                KeyBoard.append([InlineKeyboardButton(f"🌸Convert Preset - {convert_preset}🌸", callback_data="lol-mpset")])
                presets = ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']
                WX1 = []
                WX2 = []
                WX3 = []
                zz = 1
                for pp in presets:
                    if convert_preset!=pp:
                        datam = pp
                    else:
                        datam = f"{str(pp)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=f'cnvpreset_{str(pp)}')
                    if zz<4:
                            WX1.append(keyboard)
                    elif zz<7:
                            WX2.append(keyboard)
                    else:
                            WX3.append(keyboard)
                    zz+=1
                KeyBoard.append(WX1)
                KeyBoard.append(WX2)
                KeyBoard.append(WX3)
                crfs = [0, 3, 6, 9, 12, 15, 18, 21, 23, 24, 27, 28, 30, 33, 36, 39, 42, 45, 48, 51]
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🌸Use Convert CRF - {str(use_crf_convert)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"usecnvcrf_{str(x)}"
                    if use_crf_convert!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                KeyBoard.append([InlineKeyboardButton(f"🌸Convert CRF - {convert_crf}🌸", callback_data="lol-wcrf")])
                CCRP1 = []
                CCRP2 = []
                CCRP3 = []
                CCRP4 = []
                CCRP5 = []
                zz = 1
                for x in crfs:
                    vlue = f"cnvcrf_{str(x)}"
                    if int(convert_crf)!=int(x):
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    if zz<5:
                            CCRP1.append(keyboard)
                    elif zz<9:
                            CCRP2.append(keyboard)
                    elif zz<13:
                            CCRP3.append(keyboard)
                    elif zz<17:
                        CCRP4.append(keyboard)
                    else:
                        CCRP5.append(keyboard)
                    zz+=1
                KeyBoard.append(CCRP1)
                KeyBoard.append(CCRP2)
                KeyBoard.append(CCRP3)
                KeyBoard.append(CCRP4)
                KeyBoard.append(CCRP5)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🌸Map Converted Subs - {str(convert_map)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"cnvsmap_{str(x)}"
                    if convert_map!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = [True, False]
                KeyBoard.append([InlineKeyboardButton(f"🌸Encode Converted Video - {str(encode_convert)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encodecnv_{str(x)}"
                    if encode_convert!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                streams = ['libx265', 'libx264']
                KeyBoard.append([InlineKeyboardButton(f"🌸WaterMark Encoder - {str(convert_encoder)}🌸", callback_data="lol-s")])
                st = []
                for x in streams:
                    vlue = f"encodercnv_{str(x)}"
                    if convert_encoder!=x:
                        datam = f"{str(x)}"
                    else:
                        datam = f"{str(x)} 🟢"
                    keyboard = InlineKeyboardButton(datam, callback_data=vlue)
                    st.append(keyboard)
                KeyBoard.append(st)
                try:
                    await callback_query.message.edit(
                        text="Settings",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(KeyBoard))
                except Exception as e:
                    print(e)
                return