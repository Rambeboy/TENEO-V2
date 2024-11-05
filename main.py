import os
import aiohttp
import asyncio
from colorama import Fore, Style
from datetime import datetime


black = Fore.LIGHTBLACK_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
red = Fore.LIGHTRED_EX
white = Fore.LIGHTWHITE_EX
magenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL


class TeneoXD:
    def __init__(self):
        self.wss_url = "wss://secure.ws.teneo.pro/websocket"

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}[{now}]{reset} {msg}{reset}")

    async def connect(self, userid):
        max_retry = 10
        retry = 1
        self.ses = aiohttp.ClientSession()
        while True:
            try:
                if retry >= max_retry:
                    self.log(f"{yellow}max retrying reacted, try again later 1")
                    return
                async with self.ses.ws_connect(
                    url=f"{self.wss_url}?userId={userid}&version=v0.2"
                ) as wss:
                    retry = 1
                    self.log(f"{green}connect to {white}websocket {green}server")
                    while True:
                        msg = await wss.receive_json(timeout=10)
                        point_today = msg.get("pointsToday")
                        point_total = msg.get("pointsTotal")
                        self.log(
                            f"{green}point today : {white}{point_today} {magenta}| {green}point total : {white}{point_total}"
                        )
                        for i in range(90):
                            await wss.send_json({"type": "PING"})
                            self.log(f"{white}send {green}PING {white}server !")
                            await countdown(10)
            except KeyboardInterrupt:
                await self.ses.close()
            except Exception as e:
                self.log(f"{red}error : {white}{e}")
                retry += 1
                continue


async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"waiting for {hour}:{minute}:{seconds} ", flush=True, end="\r")
        await asyncio.sleep(1)


async def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        f"""
    {magenta}╔═╗╔╦╗╔═╗  {green}╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐
    {magenta}╚═╗ ║║╚═╗  {green}╠═╝├┬┘│ │ │├┤ │   │ 
    {magenta}╚═╝═╩╝╚═╝  {green}╩  ┴└─└─┘└┘└─┘└─┘ ┴ 
    
    {green}Github: {white}github.com/AkasakaID
          """
    )
    if not os.path.exists("userid.txt"):
        print(f"{red}error: {white}userid.txt file is not found, run setup.py first !")
        exit()
    userid = open("userid.txt").read()
    await asyncio.create_task(TeneoXD().connect(userid=userid))


if __name__ == "__main__":
    try:
        if os.name == "nt":
            loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(loop=loop)
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()
