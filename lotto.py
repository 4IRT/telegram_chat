import random

def getLotto():
    winner = [1, 15, 19, 23, 28, 42]

    lotto = sorted(random.sample(range(1, 46), 6))

    cnt = len(set(winner) & set(lotto))

    # 6, 1등
    # 5, 3등
    # 4, 4등
    # 3, 5등

    rank = ''
    if cnt == 6:
        rank = '1등'
    elif cnt == 5:
        rank = '3등'
    elif cnt == 4:
        rank = '4등'
    elif cnt == 3:
        rank = '5등'
    else:
        rank = '꽝'

    print(f'{cnt}, {rank}')

# n = 0
# while(n<1000) {

# }

n = 0
while n < 100:
    # 반복할 코드
    getLotto()
    n += 1