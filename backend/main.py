import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.main import app, handler


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
