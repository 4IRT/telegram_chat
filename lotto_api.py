import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'

res = requests.get(url)

# json을 python dictionary로 파싱
data = res.json()

winner = []

# js의 push와 거의 동일
for i in range(1, 7):
    winner.append(data[f'drwtNo{i}'])

print(winner)