import requests
from bs4 import BeautifulSoup

# '''
# /**
#  * 获取图片
#  */
# '''
# header = {
#     'Referer': 'https://ssr1.scrape.center/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
# }

# response = requests.get(
#     'https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c', 
#     headers=header, 
#     proxies={'http': None, 'https': None}  # 如果开了vpn需要这行代码来禁用代理
# )

# with open('pac_hong.jpg', 'wb') as file:
#     file.write(response.content)

# '''
# /**
#  * 获取网页
#  */
# '''
# header = {
#     'Referer': 'https://.scrape.center/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
# }

# response = requests.get(
#     'https://ssr1.scrape.center/',
#     headers=header,
#     proxies={'http': None, 'https': None}  # 如果开了vpn需要这行代码来禁用代理
# )

# with open('pac_hong.html', 'w', encoding='utf-8') as file:
#     file.write(response.text)  # 获取所有内容

'''
/**
 * 获取网页内容
 */
'''
header = {
    'Referer': 'https://.scrape.center/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://ssr1.scrape.center/',
    headers=header,
    proxies={'http': None, 'https': None}  # 如果开了vpn需要这行代码来禁用代理
)

soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all(name='div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')

for i in range(len(result)):
    with open('movie.txt', 'a', encoding='utf-8') as f:
        f.write(result[i].h2.string + '\n')  # 获取标题

        button_list = result[i].find_all(name='button', class_='el-button category el-button--primary el-button--mini')
        for btn in button_list:
            f.write(btn.span.string + '\n')  # 获取标签
            
        info_list = result[i].find_all(name='div', class_='m-v-sm info')
        for info in info_list:
            span_list = info.find_all(name='span')
            for s in span_list:
                if s.string != ' / ':
                    f.write(s.string + '\n')  # 获取标签
                    
        score = soup.find_all(name='p', class_='score m-t-md m-b-n-sm')
        f.write(score[i].string.strip() + '\n')  # 获取评分
        f.write('-' * 50 + '\n')