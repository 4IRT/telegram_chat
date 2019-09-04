const axios = require('axios')

const text = 'this is a msg'
const url = `https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=${text}`

axios.get(url)
    .then(res => {
        console.log(res)
    })