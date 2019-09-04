# const _ = require('lodash')
import random

# const foods = ['피자', '타코벨', '장어', '치킨']
foods = ['피자', '타코벨', '장어', '치킨']

# console.log(_.sample(foods))
print(random.choice(foods))

matzip = {
    '백운봉 막국수': '이베리코 돼지고기', 
    '고갯마루': '닭도리탕', 
    '대우식당': '부대찌개'
}

# matzip.고갯마루 (X)
print(matzip['고갯마루'])