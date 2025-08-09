from fastapi import FastAPI, HTTPException
from models import Student
from typing import List

# student database for storing student details as a list of pydantic objects
student_db: List[Student] = []

app = FastAPI(title="Student Management System", description="A simple CRUD API for managing students using FastAPI.")

# main route endpoint
@app.get("/")
def home():
    return {'message':'Hi, Welcome to Student Management System using FastAPI.'}

# 1. view all student details
@app.get('/view_all', response_model=List[Student])
def view_all_students():
    return student_db

# 2. view any selected student based on student id
@app.get('/view_std/{std_id}', response_model=Student)
def view_student(std_id: int):
    for student in student_db:
        if student.std_id == std_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found.")

# 3. add any new student
@app.post("/add_std")
def add_student(new_std: Student):
    for student in student_db:
        if student.std_id == new_std.std_id:
            raise HTTPException(status_code=409, detail="Student already exists.")
    student_db.append(new_std)
    return {'message':'student added'}

# 4. update any old student data
@app.put('/update_std/{std_id}')
def update_student(std_id: int, updated_std: Student):
    for index, student in enumerate(student_db):
        if student.std_id == std_id:
            student_db[index] = updated_std
            return {'message':'Student Updated'}
    raise HTTPException(status_code=404, detail="Student not found.")

# 5. delete any student
@app.delete('/delete_std/{std_id}')
def delete_student(std_id: int):
    for index, student in enumerate(student_db):
        if student.std_id == std_id:
            del student_db[index]
            return {"message":'Student Deleted'}
    raise HTTPException(status_code=404, detail="Student not found.")