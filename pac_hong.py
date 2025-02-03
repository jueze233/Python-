import requests

header = {
    'Referer': 'https://ssr1.scrape.center/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c', 
    headers=header, 
    proxies={'http': None, 'https': None}  # 如果开了vpn需要这行代码来禁用代理
)

print(response.text)

with open('pac_hong.jpg', 'wb') as file:
    file.write(response.content)