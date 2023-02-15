# import statements
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOFStudentEntity
from bson import ObjectId

student_router = APIRouter()


@student_router.get('/hello')
async def hello_word():
    return "Hello world"


# getting all students
@student_router.get('/students')
async def find_all_students():
    return listOFStudentEntity(connection.local.student.find())


# getting one students with maching Id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


# creating a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOFStudentEntity(connection.local.student.find())


# update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    # find the student and than update it with new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


# Delete a student
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    # dinfs the student deletes it and also returns the same student_object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
