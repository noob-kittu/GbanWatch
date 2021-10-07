from Sibyl_System import System, system_cmd
import os
import sys
import subprocess


@System.on(system_cmd(pattern=r"GbanWatch Gitpull"))
async def gitpull(event):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await event.reply("Git pulled probably.")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@System.on(system_cmd(pattern=r"GbanWatch Restart"))
async def reboot(event):
    if event.fwd_from:
        return
    await event.reply("Restarting.....")
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@System.on(system_cmd(pattern=r"GbanWatch Shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await event.reply("Shutting Down... ")
    await System.disconnect()
