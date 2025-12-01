#!/usr/bin/env python3
"""
Simple startup script for the FastAPI backend
"""
import uvicorn

if __name__ == "__main__":
    print("Starting AI Customer Support Chatbot Backend...")
    print("API will be available at http://localhost:8000")
    print("API docs available at http://localhost:8000/docs")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

