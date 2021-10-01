const express = require('express');
const req = require('express/lib/request');
const app = express();
const port = 3000;

app.use(express.json());

const geol = [];
const locs = [];

 
app.get("/", (req, res) => {
  res.end('welcome to the dashboard of a index \n Developed by mehedi');
});

app.get("/t_player_api",(req,res)=>{
    res.send(geol);
});

app.get('/t_player_api/:id',(req,res)=>{
    const geo = geol.find(c =>c.id===parseInt(req.params.id));
    if(!geo) res.status(404).send('The given id is not found ');
    res.send('geo');
});

app.post("/t_player_api",(req,res)=>{
    const geo = {
        id:geol.length +1,
        name:req.body.name,
        phone:req.body.phone
    };
    geol.push(geo);
    res.send(geo);
});

app.get('/t_player_location',(req,res)=>{
    res.send(locs);
});
app.get('/t_player_location',(req,res)=>{
    const loc = locs.find(c=>c.id===parseInt(req.params.id));
    if(!loc) res.status(404).send('id not found');
    res.send(loc);
})
app.post('/t_player_location',(req,res)=>{
    const loc = {
        id:locs.length+1,
        latitute:req.body.latitute,
        logitute:req.body.longitute
    };
    locs.push(loc);
    res.send(loc);
});


app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`)
  });
