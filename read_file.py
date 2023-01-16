#!/usr/bin/env python

"""This is the python CLI/Util used to get github file content for the given org, repo, and file path.

This module takes below parameters.
org -- GitHub org (Example: kumvijaya)
repo -- Repository name (Example: test-repo)
path -- File path in the repo (Example: folder1/test.yaml)

This connects to Github API, gets the file content with given org, repo, and file path.
It requires env variable 'GITHUB_TOKEN' to be set.
"""

import base64
import os, requests
import argparse

parser = argparse.ArgumentParser(
    description='Gets github file content'
)
parser.add_argument(
    '-o',
    '--org',
    required=True,
    help='Provide org name e.g. kumvijaya')
parser.add_argument(
    '-r',
    '--repo',
    required=True,
    help='Provide repo name e.g. test-repo')
parser.add_argument(
    '-p',
    '--path',
    required=True,
    help='Provide path name e.g. folder1/test.yaml')

args = parser.parse_args()
org = args.org
repo = args.repo
path = args.path

def github_read_file(github_org, repository_name, file_path):
    """Gets github api requets header

    Args:
        github_org (str): github org name
        repository_name (str): repo name
        file_path (str): file path 

    Returns:
        str: file content
    """
    github_token = os.environ['GITHUB_TOKEN']
    headers = get_gh_header(github_token)
    url = f'https://api.github.com/repos/{github_org}/{repository_name}/contents/{file_path}'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    file_content = data['content']
    file_content_encoding = data.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()
    return file_content

def get_gh_header(gh_token):
    """Gets github api requets header

    Args:
        gh_token (str): auth token

    Returns:
        map: header
    """
    return {'Authorization': 'token {}'.format(gh_token)}


try:
    file_content = github_read_file(org, repo, path)
    print(file_content)
except Exception as e:
    print(e)


