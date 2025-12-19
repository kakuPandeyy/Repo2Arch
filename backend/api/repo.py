from fastapi import APIRouter, HTTPException
from schema.repo_schema import RepoCloneRequest
from services.git_service import clone_repository

router = APIRouter(prefix="/repo", tags=["Repository"])

@router.post("/clone")
def clone_repo(data: RepoCloneRequest):
    try:
        result = clone_repository(data.repo_url)
        return {
            "message": result["message"],
            "repo_detail": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
