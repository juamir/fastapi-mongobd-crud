# Imports
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

client_apps = ['http://localhost:3000']  # Our REACT app will be running on this IP and PORT

# Create app
app = FastAPI()

# Register your router
app.include_router(student_router)

# Register App with CORS middleware to allow resource shsaring between different domians/origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    # allow_credential=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
