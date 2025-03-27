const express = require('express');
const router = express.Router();
const Student = require('../models/Student');

router.post('/add',async(req,res)=>{
    try{
        const { name , studentId , section , faceEmbedding} = req.body;

        //checl if student already exists

        const existingStudent = await Student.findOne({ studentId});
        if(existingStudent){
            return res.status(400).json({ message : " Student already exists"});

        }

        //create new student


        const newStudent = new Student({ name , studentId , section,  faceEmbedding});
        console.log("Student added successfully:", newStudent);
        await newStudent.save();

        res.status(201).json({ message : "student added successfully"});

    }
    catch(error){
        res.status(500).json({ messaage : "Error adding student", error});
    }
});

module.exports = router;