import requests

url = "https://ld246.com/notifications/unread/count?_=1716778079921"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'cookie': 'Hm_lvt_5aca0a0f4cab53fc6513525f5fe51343=1716778020; symphony=b1d0d1ad98acdd5d7d846d4359048a923f932962125e7ad0c9db814d5942879467b648f693d6a11336bcaa8b1bee42090ae1061a025b6f16d8afdc6baac0c1129f62ce384f54ec3360273c1f53642adeb2e8393ba3004d89b181928878c89c24e638591a9180e59737c43151f772d13ac50a096777e1b3fd61b763e354942347967fa36ebbb8350476d574acef405aa70f2379a06fd6a29cce55d70888ea721909d43654aa4f32fc087b3e12f785c45d66d9a448e12caba80c3a5da54912bb2c1bdce665be3d2f3b9498e6c812aabe4acfbb3dc839f0a810f6128ce0cb9108b5e9659cc36f2b2dea4c79e05d20c04344; Hm_lpvt_5aca0a0f4cab53fc6513525f5fe51343=1716778080; symphony=b1d0d1ad98acdd5d7d846d4359048a923f932962125e7ad0c9db814d5942879467b648f693d6a11336bcaa8b1bee42090ae1061a025b6f16d8afdc6baac0c1129f62ce384f54ec3360273c1f53642adeb2e8393ba3004d89b181928878c89c24e638591a9180e59737c43151f772d13accec761b54f6946543c36725db87b0a6967fa36ebbb8350476d574acef405aa70f2379a06fd6a29cce55d70888ea721909d43654aa4f32fc087b3e12f785c45d66d9a448e12caba80c3a5da54912bb2c1bdce665be3d2f3b9498e6c812aabe4ac4a12cb985f0a72a01c9643e48371a70d801c66cdc4f63ffd1fb1d028cd5ca25',
  'priority': 'u=1, i',
  'referer': 'https://ld246.com/activity/checkin',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

