import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm  # 导入 tqdm

moive_info = {'电影名字': [], '类型': [], '国家': [], '时长': [], '上映时间': [], '电影评分': []}
header = {
    'Referer': 'https://.scrape.center/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}
print('开始爬取')

for page in tqdm(range(1, 11), desc='爬取进度'):  # 使用 tqdm 包裹 range
    response = requests.get(
        'https://ssr1.scrape.center/page/%d' %page,
        headers=header,
        proxies={'http': None, 'https': None}  # 如果开了vpn需要这行代码来禁用代理
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all(name='div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')

    for i in range(len(result)):
        moive_info['电影名字'].append(result[i].h2.string)  

        button_list = result[i].find_all(name='button', class_='el-button category el-button--primary el-button--mini')
        moive_type = []
        for btn in button_list:
            moive_type.append(btn.span.string)
        moive_type = ','.join(moive_type)  
        moive_info['类型'].append(moive_type)
            
        info_list = result[i].find_all(name='div', class_='m-v-sm info')
        span_list = info_list[0].find_all(name='span')
        moive_info['国家'].append(span_list[0].string)
        moive_info['时长'].append(span_list[2].string)
        span_list = info_list[1].find_all(name='span')
        if len(span_list) > 0:
            moive_info['上映时间'].append(span_list[0].string)
        else:
            moive_info['上映时间'].append('未知')
                    
        score = soup.find_all(name='p', class_='score m-t-md m-b-n-sm')
        moive_info['电影评分'].append(score[i].string.strip() )  
            
data = pd.DataFrame(moive_info)
data.to_excel('./info.xlsx', index=False)
print('爬取完毕')