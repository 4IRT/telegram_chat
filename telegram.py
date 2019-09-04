import requests
from decouple import config

chat_id = ''
text = ''
base_url = 'https://api.telegram.org'
token = config('TOKEN')

print(token)

url = f'{base_url}/bot{token}/getUpdates'

print(url)

"""
getUpdates 요청을 통해 받아온 응답에서 id를 뽑아내어
sendMessage를 통해 메세지 보내기

1. 한 사람에게만 보내기(첫번째로 메세지 보낸사람)
2. 나에게 메세지 보낸 모든 사람에게 보내기
"""

res = requests.get(url)
data = res.json()

chat_id = data['result'][0]['message']['chat']['id']

senders = []

# 여러개가 있다.
for result in data['result']:
    senders.append(result['message']['chat']['id'])

receivers = set(senders)

print(receivers)
text = '오늘 정말 수고 많으셨습니다. 다음에 뵈요 :)'

for chat_id in receivers:
    url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(url)