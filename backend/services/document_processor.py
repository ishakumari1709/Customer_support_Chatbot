import io
import os
from typing import List

# Try to import text splitter with fallbacks
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    # Fallback: simple text splitter implementation
    class RecursiveCharacterTextSplitter:
        def __init__(self, chunk_size=1000, chunk_overlap=200, length_function=len):
            self.chunk_size = chunk_size
            self.chunk_overlap = chunk_overlap
            self.length_function = length_function
        
        def split_text(self, text: str):
            """Split text into chunks with overlap"""
            chunks = []
            start = 0
            text_length = self.length_function(text)
            
            while start < text_length:
                end = min(start + self.chunk_size, text_length)
                chunk = text[start:end]
                chunks.append(chunk)
                
                # Move start position with overlap
                start = end - self.chunk_overlap
                if start >= text_length:
                    break
                # Ensure we don't go backwards
                if start <= 0:
                    start = end
            
            return chunks

# Import document processing libraries with error handling
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None
    print("Warning: PyPDF2 not installed. PDF processing will not work.")

try:
    from docx import Document
except ImportError:
    Document = None
    print("Warning: python-docx not installed. DOCX processing will not work.")

# aiofiles is optional for async file operations
try:
    import aiofiles
except ImportError:
    aiofiles = None


class DocumentProcessor:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    async def process_document(self, content: bytes, filename: str, content_type: str) -> List[dict]:
        """Process uploaded document and return chunks"""
        text = ""
        
        if content_type == "application/pdf" or filename.endswith(".pdf"):
            text = await self._extract_pdf_text(content)
        elif content_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", 
                              "application/msword"] or filename.endswith((".docx", ".doc")):
            text = await self._extract_docx_text(content)
        else:
            # Try to decode as plain text
            try:
                text = content.decode('utf-8')
            except:
                raise ValueError(f"Unsupported file type: {content_type}")
        
        if not text.strip():
            raise ValueError("No text content found in document")
        
        return await self.process_text(text, filename)
    
    async def _extract_pdf_text(self, content: bytes) -> str:
        """Extract text from PDF"""
        if PyPDF2 is None:
            raise ImportError("PyPDF2 is not installed. Please install it with: pip install PyPDF2")
        
        pdf_file = io.BytesIO(content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    async def _extract_docx_text(self, content: bytes) -> str:
        """Extract text from DOCX"""
        if Document is None:
            raise ImportError("python-docx is not installed. Please install it with: pip install python-docx")
        
        docx_file = io.BytesIO(content)
        doc = Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    
    async def process_text(self, text: str, source: str) -> List[dict]:
        """Split text into chunks with metadata"""
        chunks = self.text_splitter.split_text(text)
        
        chunk_docs = []
        for i, chunk in enumerate(chunks):
            chunk_docs.append({
                "content": chunk,
                "metadata": {
                    "source": source,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                }
            })
        
        return chunk_docs

