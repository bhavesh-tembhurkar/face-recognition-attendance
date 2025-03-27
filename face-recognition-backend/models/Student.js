const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const studentSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    studentId: {
        type: String,
        required: true,
        unique: true
    },
    section: {
        type: String,
        required: true
    },
    faceEmbedding: {
        type: Array,
        required: true
    }
}, { timestamps: true });

const Student = mongoose.model('Student', studentSchema);
module.exports = Student;