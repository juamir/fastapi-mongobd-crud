#Imports
from fastapi import FastAPI
from routes.student import student_router

#Create app
app = FastAPI()

#Register your router
app.include_router(student_router)
