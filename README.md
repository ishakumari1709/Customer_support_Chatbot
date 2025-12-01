# Customer_support_Chatbot
# 🤖 AI Customer Support Chatbot

A powerful RAG (Retrieval Augmented Generation) based customer support chatbot that can answer questions from uploaded documents using AI. Built with FastAPI, LangChain, ChromaDB, and HuggingFace.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [How It Works](#-how-it-works)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Project Structure](#-project-structure)

## ✨ Features

- 📄 **Document Processing**: Upload and process PDF, DOCX files
- 🖼️ **OCR Support**: Extract text from screenshots and images using Tesseract or EasyOCR
- 🔍 **RAG Pipeline**: Semantic search using vector embeddings to find relevant document chunks
- 💬 **Intelligent Chat**: Get context-aware answers based on uploaded documents
- 🗄️ **Session Management**: Track multiple chat sessions with history
- 🧠 **Multiple LLM Options**: Use HuggingFace API or local models
- 🆓 **Free & Open Source**: All components are free and open-source
- 🔒 **Session Isolation**: Each session has its own vector database collection

## 🏗️ Architecture

### System Overview

```
User Uploads Document
        ↓
Document Processing (PDF/DOCX/Image)
        ↓
Text Extraction & Chunking
        ↓
Generate Embeddings (Sentence Transformers)
        ↓
Store in Vector Database (ChromaDB)
        ↓
User Asks Question
        ↓
Semantic Search (Find Relevant Chunks)
        ↓
Build Context from Top Chunks
        ↓
Generate Answer (LLM: HuggingFace API or Local)
        ↓
Return Response with Sources
```

### Components

1. **Document Processor**: Extracts text from PDFs, DOCX files
2. **OCR Service**: Extracts text from images/screenshots
3. **RAG Service**: Manages embeddings, vector search, and LLM generation
4. **Database**: SQLite for chat history, ChromaDB for vector storage
5. **API Server**: FastAPI REST API for all operations

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **LangChain**: RAG pipeline and LLM integration
- **ChromaDB**: Vector database for embeddings
- **Sentence Transformers**: Text embeddings (all-MiniLM-L6-v2)
- **HuggingFace**: LLM inference (API or local models)
- **SQLAlchemy**: Database ORM
- **PyPDF2 / python-docx**: Document processing
- **Tesseract / EasyOCR**: OCR for images

### Database
- **SQLite**: Chat sessions and message history
- **ChromaDB**: Vector embeddings storage

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Node.js for frontend

### 1. Clone or Download the Project

```bash
# Navigate to project directory
cd customer_support
```

### 2. Set Up Backend

```bash
# Navigate to backend folder
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Note**: First installation may take 5-10 minutes as it downloads AI models.

### 3. Configure API Key (Optional but Recommended)

1. Get a free API key from [HuggingFace](https://huggingface.co/settings/tokens)
2. Create `backend/.env` file:
   ```
   HUGGINGFACE_API_KEY=your_api_key_here
   ```

### 4. Start the Server

```bash
python start.py
```

The API will be available at:
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📦 Installation

### Detailed Installation Steps

#### Step 1: Python Environment

```bash
# Check Python version (should be 3.8+)
python --version

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

#### Step 2: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

This installs:
- FastAPI and Uvicorn (web server)
- LangChain and LangChain Community (RAG framework)
- ChromaDB (vector database)
- Sentence Transformers (embeddings)
- PyPDF2, python-docx (document processing)
- EasyOCR (OCR)
- And other dependencies

#### Step 3: Verify Installation

```bash
# Test if server starts
python start.py
```

You should see:
```
Starting AI Customer Support Chatbot Backend...
API will be available at http://localhost:8000
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## ⚙️ Configuration

### Environment Variables

Create `backend/.env` file:

```env
# HuggingFace API Key (Optional but Recommended)
# Get from: https://huggingface.co/settings/tokens
HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Database URL (Optional - defaults to SQLite)
DATABASE_URL=sqlite:///./chatbot.db
```

### LLM Configuration Options

The system supports three LLM options:

1. **HuggingFace Inference API** (Recommended)
   - Set `HUGGINGFACE_API_KEY` in `.env`
   - Fast, high-quality responses
   - Free tier available
   - No local resources needed

2. **Local Model** (Fallback)
   - Automatically used if no API key
   - Uses GPT-2 (small, fast)
   - Runs on CPU
   - Requires model download (~500MB)

3. **Smart Fallback** (If LLM fails)
   - Context-based responses
   - Extracts relevant information from documents
   - Works without any LLM

### OCR Configuration

Two OCR options available:

1. **Tesseract OCR** (Faster)
   - Requires system installation
   - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Mac: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`

2. **EasyOCR** (More Accurate)
   - No system installation needed
   - Automatically installed with requirements.txt
   - Larger download (~500MB) on first use

## 📚 API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### 1. Create Session

Create a new chat session.

```http
POST /api/sessions
Content-Type: application/json

{
  "title": "New Chat"
}
```

**Response:**
```json
{
  "id": "uuid-here",
  "title": "New Chat",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

#### 2. Upload Document

Upload a PDF or DOCX file for processing.

```http
POST /api/upload/document?session_id={session_id}
Content-Type: multipart/form-data

file: [your-file.pdf]
```

**Response:**
```json
{
  "message": "Document processed successfully",
  "chunks": 5,
  "session_id": "uuid-here"
}
```

#### 3. Upload Screenshot (with OCR)

Upload an image to extract text using OCR.

```http
POST /api/upload/screenshot?session_id={session_id}
Content-Type: multipart/form-data

file: [your-image.png]
```

**Response:**
```json
{
  "message": "Screenshot processed successfully",
  "text": "Extracted text from image...",
  "chunks": 3,
  "session_id": "uuid-here"
}
```

#### 4. Send Chat Message

Ask a question and get an AI response.

```http
POST /api/chat
Content-Type: application/json

{
  "session_id": "uuid-here",
  "message": "What is the company's return policy?"
}
```

**Response:**
```json
{
  "response": "Based on the documents, the return policy is...",
  "sources": ["document.pdf"],
  "session_id": "uuid-here"
}
```

#### 5. Get Session Messages

Retrieve all messages for a session.

```http
GET /api/sessions/{session_id}/messages
```

**Response:**
```json
{
  "messages": [
    {
      "id": "uuid-here",
      "role": "user",
      "content": "What is the company?",
      "created_at": "2024-01-01T00:00:00"
    },
    {
      "id": "uuid-here",
      "role": "assistant",
      "content": "Based on the documents...",
      "created_at": "2024-01-01T00:00:01"
    }
  ]
}
```

### Interactive API Documentation

Visit http://localhost:8000/docs for interactive Swagger UI documentation where you can test all endpoints directly.

## 🔄 How It Works

### Document Processing Flow

1. **Upload**: User uploads a PDF, DOCX, or image
2. **Extraction**: Text is extracted from the document
3. **Chunking**: Text is split into smaller chunks (1000 characters with 200 overlap)
4. **Embedding**: Each chunk is converted to a vector embedding
5. **Storage**: Embeddings are stored in ChromaDB vector database

### Query Processing Flow

1. **Question**: User asks a question
2. **Embedding**: Question is converted to a vector embedding
3. **Search**: Vector similarity search finds top 3 most relevant chunks
4. **Context**: Relevant chunks are combined into context
5. **Generation**: LLM generates answer based on context
6. **Response**: Answer is returned with source document names

### RAG Pipeline Details

- **Embeddings Model**: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
- **Vector Database**: ChromaDB (local file-based)
- **Search Method**: Cosine similarity
- **Top K Results**: 3 most relevant chunks
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters

## 🚢 Deployment

### Deploy Backend to Render

1. **Create Render Account**: Sign up at [render.com](https://render.com)

2. **Create New Web Service**:
   - Connect your GitHub repository
   - Select "Python 3" environment
   - Build command: `pip install -r backend/requirements.txt`
   - Start command: `cd backend && python start.py`

3. **Add Environment Variables**:
   - `HUGGINGFACE_API_KEY`: Your HuggingFace API key
   - `PYTHON_VERSION`: 3.11

4. **Deploy**: Click "Create Web Service"

### Deploy Frontend to Vercel

1. **Create Vercel Account**: Sign up at [vercel.com](https://vercel.com)

2. **Import Project**:
   - Connect your GitHub repository
   - Root directory: `project`
   - Framework preset: Vite

3. **Environment Variables**:
   - `VITE_API_URL`: Your Render backend URL

4. **Deploy**: Click "Deploy"

### Environment Variables for Production

**Backend (.env):**
```env
HUGGINGFACE_API_KEY=your_key_here
DATABASE_URL=sqlite:///./chatbot.db
```

**Frontend (.env):**
```env
VITE_API_URL=https://your-backend.onrender.com
```

## 🐛 Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'uvicorn'"

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### 2. "ChromaDB schema error: no such column: collections.topic"

**Solution:**
- The system automatically creates a new database directory
- Old database at `./chroma_db` can be deleted after stopping the server
- Restart the server to use the new database

#### 3. "MemoryError" when processing large documents

**Solution:**
- The system automatically limits document size
- Large documents are truncated with a warning
- Consider splitting very large documents

#### 4. "HuggingFace API calls failing"

**Solution:**
- Check your API key is correct in `backend/.env`
- Verify API key starts with `hf_`
- System will use smart fallback if API fails
- Check HuggingFace service status

#### 5. "OCR not working"

**Solution:**
- Install Tesseract OCR on your system, OR
- System will automatically use EasyOCR (no installation needed)
- First OCR use downloads models (~500MB)

#### 6. "Port 8000 already in use"

**Solution:**
- Stop other services using port 8000
- Or change port in `start.py`:
  ```python
  uvicorn.run("main:app", host="0.0.0.0", port=8001)
  ```

### Getting Help

1. Check terminal logs for error messages
2. Visit http://localhost:8000/docs for API testing
3. Verify all dependencies are installed
4. Check environment variables are set correctly

## 📁 Project Structure

```
customer_support/
├── backend/                    # Backend API
│   ├── main.py                # FastAPI application
│   ├── start.py               # Server startup script
│   ├── database.py            # Database configuration
│   ├── models.py              # SQLAlchemy models
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   ├── services/              # Core services
│   │   ├── document_processor.py  # PDF/DOCX processing
│   │   ├── ocr_service.py        # OCR functionality
│   │   └── rag_service.py         # RAG pipeline
│   ├── chroma_db/            # Vector database (auto-created)
│   └── chatbot.db            # SQLite database (auto-created)
│
└── project/                   # Frontend (React + Vite)
    ├── src/                   # Source code
    ├── package.json          # Dependencies
    └── vite.config.ts        # Vite configuration
```

## 📝 Key Files

- **backend/main.py**: FastAPI application and API routes
- **backend/services/rag_service.py**: Core RAG logic
- **backend/services/document_processor.py**: Document processing
- **backend/requirements.txt**: All Python dependencies
- **backend/.env**: Environment variables (create this)

## 🎯 Usage Examples

### Using cURL

#### Create a Session
```bash
curl -X POST "http://localhost:8000/api/sessions" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Chat"}'
```

#### Upload a Document
```bash
curl -X POST "http://localhost:8000/api/upload/document?session_id=YOUR_SESSION_ID" \
  -F "file=@document.pdf"
```

#### Ask a Question
```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "YOUR_SESSION_ID",
    "message": "What is the company about?"
  }'
```

### Using Python

```python
import requests

# Create session
response = requests.post("http://localhost:8000/api/sessions", 
                        json={"title": "My Chat"})
session_id = response.json()["id"]

# Upload document
with open("document.pdf", "rb") as f:
    files = {"file": f}
    requests.post(f"http://localhost:8000/api/upload/document?session_id={session_id}",
                  files=files)

# Ask question
response = requests.post("http://localhost:8000/api/chat",
                        json={"session_id": session_id,
                              "message": "What is the company about?"})
print(response.json()["response"])
```

## 🔐 Security Notes

- API keys should be kept in `.env` file (not committed to git)
- `.env` is in `.gitignore` by default
- For production, use environment variables on your hosting platform
- Consider adding authentication for production use

## 📊 Performance

- **First Run**: Downloads models (~500MB-2GB) - takes 5-10 minutes
- **Subsequent Runs**: Fast startup (< 10 seconds)
- **Document Processing**: ~1-5 seconds per document
- **Query Response**: ~2-5 seconds (with HuggingFace API)
- **Vector Search**: < 1 second

## 🆓 Free Tier Limits

- **HuggingFace API**: Free tier available with rate limits
- **ChromaDB**: Unlimited local storage
- **SQLite**: Unlimited local storage
- **All Models**: Free and open-source

## 📄 License

This project uses free and open-source components. Check individual package licenses for details.

## 🙏 Acknowledgments

- **LangChain**: RAG framework
- **ChromaDB**: Vector database
- **HuggingFace**: AI models and API
- **FastAPI**: Web framework
- **Sentence Transformers**: Embeddings

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review API documentation at http://localhost:8000/docs
3. Check terminal logs for detailed error messages

---

**Built with ❤️ using FastAPI, LangChain, ChromaDB, and HuggingFace**

