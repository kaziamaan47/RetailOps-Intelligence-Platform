from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for Fikxi, a multilingual local services marketplace.",
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "status": "running",
        "version": settings.app_version,
        "environment": settings.app_env,
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "environment": settings.app_env,
    }