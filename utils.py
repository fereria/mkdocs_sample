import yaml
import os


def getGithubRoot():

    with open(os.getcwd() + "/mkdocs.yml", 'r') as f:
        obj = yaml.safe_load(f)
        if 'repo_url' in obj:
            return obj['repo_url']
    return ""
