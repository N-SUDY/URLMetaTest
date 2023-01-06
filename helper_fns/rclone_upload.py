from asyncio import create_subprocess_exec, create_task, FIRST_COMPLETED
from asyncio import wait as asynciowait
from asyncio.subprocess import PIPE as asyncioPIPE
from asyncio import run
import re

all_data = []
msg_data = ['Processing']
running_process = []





###########Logger###################
async def get_logs(process):
                    while True:
                                    data = await process.readline()
                                    data = data.decode().strip()
                                    mat = re.findall("Transferred:.*ETA.*", data)
                                    if mat is not None:
                                        if len(mat) > 0:
                                            nstr = mat[0].replace("Transferred:", "")
                                            nstr = nstr.strip()
                                            nstr = nstr.split(",")
                                            prg = nstr[1].strip("% ")
                                            progress = "<b>Uploaded:- {} \n{} \nSpeed:- {} \nETA:- {}</b> \n<b>Using Engine:- </b><code>RCLONE</code>".format(
                                                nstr[0], prg, nstr[2], nstr[3].replace("ETA", "")
                                            )
                                            print(progress)

                                    if data == "":
                                        blank += 1
                                        if blank == 20:
                                            break
                                    else:
                                        blank = 0


###################FFMPEG Engine#############################
async def upload_video_rclone(command):
    global all_data
    global msg_data
    all_data = []
    msg_data = ['Processing']
    process = await create_subprocess_exec(
            *command,
            stdout=asyncioPIPE,
            stderr=asyncioPIPE,
            )
    pid = process.pid
    running_process.append(pid)
    log_task = create_task(get_logs(process.stdout))
    done, pending = await asynciowait([process.wait()], return_when=FIRST_COMPLETED)
    return_code = process.returncode
    running_process.remove(pid)
    print(f"🔶Process Return Code: ", return_code)
    
    

command =  [
        "rclone",
        "copy",
        f"--config=rclone.conf",
        'toon.mkv',
        'tdtest:/',
        "-f",
        "- *.!qB",
        "--buffer-size=1M",
        "-P",
    ]

run(upload_video_rclone(command))