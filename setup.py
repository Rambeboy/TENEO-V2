import aiohttp


async def main():
    email = input("input email : ")
    password = input("input password : ")
    login_url = (
        "https://ikknngrgxuxgjhplbpey.supabase.co/auth/v1/token?grant_type=password"
    )
    login_data = {
        "email": email,
        "password": password,
        "gotrue_meta_security": {},
    }
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlra25uZ3JneHV4Z2pocGxicGV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU0MzgxNTAsImV4cCI6MjA0MTAxNDE1MH0.DRAvf8nH1ojnJBc3rD_Nw6t1AV8X_g6gmY_HByG2Mag",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlra25uZ3JneHV4Z2pocGxicGV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU0MzgxNTAsImV4cCI6MjA0MTAxNDE1MH0.DRAvf8nH1ojnJBc3rD_Nw6t1AV8X_g6gmY_HByG2Mag",
        "content-type": "application/json;charset=UTF-8",
        "origin": "chrome-extension://emcclcoaglgcpoognfiggmhnhgabppkm",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "x-client-info": "supabase-js-web/2.45.4",
        "x-supabase-api-version": "2024-01-01",
    }
    async with aiohttp.ClientSession() as client:
        result = await client.post(login_url, json=login_data, headers=headers)
        if result.status != 200:
            print(f"[x] login failure, try again later or get data manual !")
            exit()
        res = await result.json()
        userid = res.get("user", {}).get("id")
        open("userid.txt", "w").write(userid)
        print(f"[+] login success, now run main.py !")


try:
    import asyncio

    asyncio.run(main())
except KeyboardInterrupt:
    exit()
