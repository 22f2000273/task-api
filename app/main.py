import requests
from fastapi import FastAPI, HTTPException
from fuzzywuzzy import fuzz
import os
from function import *
from datetime import time
import subprocess

AIPROXY_TOKEN = None

# Load environment variables
try:
    with open(".env") as f:
        for line in f:
            l = line.strip().split("=")
            if len(l) == 2:
                key, value = l[0], l[1]
                if key == "AIPROXY_TOKEN":
                    AIPROXY_TOKEN = value
except Exception as e:
    print(f"Error reading .env: {e}")

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, Docker!"}

@app.get("/read")
async def read_file(path: str):
    if not path.startswith("/data"):
        raise HTTPException(status_code=403, detail="Access to file not allowed")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run")
async def run_task(task: str):
    try:
        task_output = get_task_output(AIPROXY_TOKEN, task).lower()
        task = task.lower()
        if "count" in task:
            day = extract_daytime(task)
            count_days(day)
            return {"status": "success", "task_output": task_output}
        elif "install" in task:
            pkgname = extract_package(task)
            correct_package = get_correct_pkgname(pkgname)
            if correct_package:
                subprocess.run(["pip", "install", correct_package], check=True)
                return {"status": "success", "task_output": task_output}
            else:
                return {"status": "Package name not recognized"}
        else:
            return {"status": "Task not implemented"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))