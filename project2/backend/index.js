const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors());

app.get('/', (req, res) => {
    res.send('Backend is working!');
});

app.listen(5001, () => {
    console.log('Server is running on port 5000');
});
