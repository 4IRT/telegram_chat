/*

axios를 활용하여 
https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874
요청을 보내,

1등 번호 6개가 담긴 winner 배열을 만들어 출력하세요.
> [1, 15, 19, 23, 28, 42]

*/

const axios = require('axios')

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=874'
axios.get(url)
    .then((res) => {
        let winner = []

        for (let i = 0; i < 6; i++) {
            winner.push(res.data[`drwtNo${i+1}`])
        }
        console.log(winner)
    })