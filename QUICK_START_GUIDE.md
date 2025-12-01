# 🚀 Quick Start Guide - Run Your Local Website

## ✅ What's Been Done

1. ✅ Backend API created and configured
2. ✅ Frontend connected to backend
3. ✅ API client created
4. ✅ All integration code updated

## 📋 Steps to Run Your Website

### Step 1: Install Frontend Dependencies

Open a terminal in the `project` folder:

```powershell
cd project
npm install
```

### Step 2: Create Frontend Environment File

Create a file `project/.env` with this content:

```
VITE_API_URL=http://localhost:8000
```

**Windows PowerShell:**
```powershell
cd project
echo "VITE_API_URL=http://localhost:8000" > .env
```

**Or manually create** `project/.env` file with the content above.

### Step 3: Start Backend Server

Open **Terminal 1**:

```powershell
cd backend
python start.py
```

Wait until you see: `Uvicorn running on http://0.0.0.0:8000`

### Step 4: Start Frontend Server

Open **Terminal 2** (new terminal):

```powershell
cd project
npm run dev
```

Wait until you see: `Local: http://localhost:5173/`

### Step 5: Open Your Website

Open your browser and go to:
**http://localhost:5173**

## 🎉 You're Done!

Your website is now running!

## 🧪 Test It Out

1. **Upload a PDF or DOCX** document
2. **Ask a question** about the document
3. **Upload a screenshot** to test OCR
4. **Chat** with the AI

## 📝 Important Files Created/Updated

- ✅ `project/src/lib/api.ts` - API client for backend
- ✅ `project/src/hooks/useChat.ts` - Updated to use FastAPI
- ✅ `project/src/App.tsx` - Updated for document uploads
- ✅ `project/.env` - Frontend environment config (you need to create this)

## ⚠️ Troubleshooting

### Frontend can't connect to backend?
- Make sure backend is running first (Step 3)
- Check `project/.env` exists with correct URL
- Restart frontend after creating `.env`

### Backend won't start?
- Install dependencies: `cd backend && pip install -r requirements.txt`
- Check API key in `backend/.env`

### Port already in use?
- Backend: Change port in `backend/start.py` (line 14)
- Frontend: Vite will automatically use next available port

## 🎯 What You Can Do Now

- Upload documents (PDF, DOCX)
- Ask questions about documents
- Upload screenshots for OCR
- Chat with AI using RAG
- View API docs at http://localhost:8000/docs

---

**Ready to go! Start with Step 1 above.** 🚀

