from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Store API",
    version="1.0.0",
    description="API documentation for Store API"
)

# Create database tables on startup
# Base.metadata.create_all(bind=engine)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Monthly Rent Analysis"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)