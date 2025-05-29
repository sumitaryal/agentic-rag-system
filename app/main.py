from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    # Initialize resources or connections here if needed
    yield
    # Cleanup resources or connections here if needed


app = FastAPI(
    title="Agentic RAG Application",
    description="A FastAPI application for Agentic RAG.",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello, Welcome to Agentic RAG Application!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
