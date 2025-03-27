const express = require('express');
const mongoose = require('mongoose');

const cors = require('cors');  //Cross-Origin Resource Sharing. 
require("dotenv").config(); //for sensitive data or info like API keys, passwords, etc. (environment variables)

const app = express();
const PORT = process.env.PORT || 8080;

//middleware 

app.use(cors());
app.use(express.json());  //JSON (JavaScript Object Notation) 

//connect to mongodb

mongoose.connect(process.env.MONGO_URI)
.then(()=> console.log("MongoDB connected Successfully"))
.catch(err=>console.log("MongoDb Connection Error",err));

//Default route

const studentRoutes = require('./routes/studentRoutes');
app.use("/api/students",studentRoutes);

app.get("/", (req,res)=>{


    res.send("Welcome to face recognition is Running ");;

});



//start server

app.listen(PORT,()=>{
    console.log(`Server is running on port ${PORT}`);
})