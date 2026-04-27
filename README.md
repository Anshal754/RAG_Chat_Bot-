# DocuMind AI — Intelligent Retrieval-Augmented Generation (RAG) Chatbot

DocuMind AI is an end-to-end AI-powered document intelligence system that allows users to upload documents and interact with them through natural language conversations.

The project implements a Retrieval-Augmented Generation (RAG) pipeline that combines semantic search, vector embeddings, document chunking, and transformer-based language models to generate context-grounded answers instead of generic chatbot responses.

Unlike traditional chatbots that rely only on model knowledge, this system retrieves relevant information from uploaded documents first and then generates responses using that retrieved context, improving factual grounding and reducing hallucinations.

---

## Overview

This project was built to simulate a lightweight private document assistant capable of:

- Understanding uploaded documents
- Creating a searchable semantic knowledge base
- Retrieving relevant information for user questions
- Generating AI-powered grounded responses
- Providing an interactive chat interface for document conversations

The system supports question answering over custom user data such as:
- Notes
- Research papers
- PDFs
- Documentation
- Resumes
- Reports
- Knowledge bases

---

## Core Features

### Document Processing Pipeline
- Upload support for PDF, TXT, DOCX and text-based files
- Automatic text extraction
- Intelligent text chunking for retrieval
- Chunk indexing into vector storage

### Semantic Search / Retrieval
- Embedding generation using Sentence Transformers
- Vector similarity search for relevant context retrieval
- Top-k chunk retrieval
- Fast and Accurate retrieval modes

### Retrieval-Augmented Generation (RAG)
- Context-aware answer generation
- Grounded responses using retrieved document chunks
- Hallucination reduction through retrieval-first prompting
- Smart fallback generation strategy for weak answers

### AI Models
- FLAN-T5 based response generation
- Dual-model setup:
  - Fast model for low-latency responses
  - Fallback larger model for better answer recovery

### Frontend Interface
- Futuristic interactive chat UI
- Document upload panel
- Real-time query interface
- Animated user experience
- Query mode selection
- Indexed document tracking

### Backend API
- FastAPI-powered backend
- Upload endpoint
- Query endpoint
- Health-check endpoint
- CORS enabled for frontend integration

---

## Architecture

Pipeline Flow:

User Upload  
↓  
Text Extraction  
↓  
Chunking  
↓  
Embedding Generation  
↓  
Vector Store Indexing  
↓  
Semantic Retrieval  
↓  
Prompt Construction  
↓  
LLM Answer Generation

This combines information retrieval with generative AI for more reliable answers.

---

## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI / NLP
- Transformers
- Sentence Transformers
- Hugging Face Models
- FLAN-T5

### Retrieval
- Vector Store / Similarity Search
- Embeddings
- Semantic Retrieval

### Frontend
- HTML
- CSS
- JavaScript

---

## Modes

### Fast Mode
Optimized for:
- Lower latency
- Lightweight retrieval
- Quick responses

### Accurate Mode
Optimized for:
- More retrieved context
- Better grounding
- Improved answer quality
- Fallback reasoning support

---

## Project Highlights
- End-to-end RAG implementation from scratch
- Custom document QA system
- AI + Search hybrid architecture
- Full-stack ML application
- Resume-worthy applied LLM project
- Practical implementation of modern GenAI concepts

---

## Use Cases
- Personal knowledge assistant
- Resume / portfolio Q&A bot
- Research assistant
- Document search assistant
- Internal company knowledge bot
- Educational tutoring assistant
- Domain-specific AI chatbot

---

## Future Improvements
Planned enhancements:
- Multi-document persistent knowledge base
- Conversation memory
- Reranking models
- Streaming responses
- Better vector databases
- Authentication and user workspaces
- Hybrid keyword + semantic retrieval
- Agentic workflows
- Cloud deployment optimization

---

## Goal of the Project
The objective of this project was to build a practical implementation of modern Retrieval-Augmented Generation systems and explore how semantic search and LLMs can be combined to create intelligent document assistants.

This project demonstrates applied skills in:
- NLP
- Information Retrieval
- LLM Integration
- Backend Development
- Full Stack AI Engineering
- RAG System Design
- 
