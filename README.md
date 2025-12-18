# Repo2Arch

### **Repo2Arch – Automatic Software Architecture & Documentation Generator**

\*\*Repo2Arch \*\* is a developer tool that analyzes a GitHub repository and automatically generates **software architecture diagrams, data models (ER-style diagrams), control/flow diagrams, and technical documentation**.

## OBJECTIVE

The goal of the project is to make **new or unfamiliar codebases easy to understand** by converting raw source code into **visual and structured representations**, without requiring manual reading of thousands of lines of code.

### This tool is especially useful for:

- Onboarding new developers
- Understanding legacy projects
- System design reviews
- Technical documentation automation

## 🎯 Problem Statement

Understanding an existing codebase is time-consuming because:

- Architecture is rarely documented
- Diagrams are outdated or missing
- Relationships between modules, services, and databases are unclear

Developers are forced to manually analyze:

- Folder structure
- Imports and dependencies
- API routes
- Database models

**Repo2Arch solves this problem by automating codebase understanding.**

## How to Run This Project DEV

1. Clone the repo

```bash
  git clone https://github.com/kakuPandeyy/Repo2Arch.git
 ```
 
2. Create virtual environment

```bash
   cd backend
   python -m venv my_env
```

3. Install dependencies
 ```bash
    pip install -r requirements.txt

```
6. Run server
  
```bash
    uvicorn main:app --reload

```