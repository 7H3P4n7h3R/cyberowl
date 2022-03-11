from git import Repo
import os 
from dotenv import load_dotenv
load_dotenv()

GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME")

PATH_OF_GIT_REPO = os.getcwd()+"\.git"  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'This is a test commit'
FILE_TO_ADD="README.md"

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(FILE_TO_ADD)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    