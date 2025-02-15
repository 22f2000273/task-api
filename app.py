from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from tasksA import *
from tasksB import *
import requests
from dotenv import load_dotenv
import os
import re
import httpx
import json
import time