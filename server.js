const express = require('express')
const app = express()
app.use(express.json())

app.get('/', (req, res) => {
    res.json({message: "Application running on port 3001"});
});

app.listen(3001, () => {
    console.log("server is running on port 3001")
})