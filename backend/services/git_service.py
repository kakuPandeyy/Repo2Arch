import os
from urllib.parse import urlparse
from git import Repo

BASE_DIR = "cloned_repos"


#extract user info for making floder name

def extract_user_repo(repo_url: str):
 
    path = urlparse(repo_url).path.strip("/")
    
    parts = path.split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    username = parts[0]
    repo_name = parts[1].replace(".git", "")

    return username, repo_name



# clone functions

def clone_repository(repo_url: str):
    username, repo_name = extract_user_repo(repo_url)

    user_dir = os.path.join(BASE_DIR, username)
    repo_dir = os.path.join(user_dir, repo_name)

    # Ensure folders exist
    os.makedirs(user_dir, exist_ok=True)

    # Avoid cloning again if repo already exists
    if os.path.exists(repo_dir):
        return {
            "message": "Repository already exists",
            "path": repo_dir
        }

    Repo.clone_from(repo_url, repo_dir)

    return {
        "message": "Repository cloned successfully",
        "username": username,
        "repo": repo_name,
        "path": repo_dir
    }