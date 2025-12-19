from pydantic import BaseModel

class RepoCloneRequest(BaseModel):
    repo_url: str
