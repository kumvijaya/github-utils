#!/usr/bin/env python

"""This is the python module used to get the content of the requested file from GitHub.

This module takes below three parameters.
owner - Provide github user/owner name e.g. kumvijaya
repo -- Provide repository name e.g. my-repo
branch  -- Provide branch name e.g. master
filepath  -- Provide file path in repo e.g. config/settings.yaml

This required GITHUB_TOKEN environment variable to be set.
This connects to GitHub via REST API (https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28), gets the requested file content.
"""

import argparse
import base64
import os, requests

parser = argparse.ArgumentParser(
    description='Gets the content of the requested file from GitHub'
)
parser.add_argument(
    '-o',
    '--owner',
    required=True,
    help='Provide github user/owner name e.g. kumvijaya')
parser.add_argument(
    '-r',
    '--repo',
    required=True,
    help='Provide repository name e.g. my-repo')
parser.add_argument(
    '-b',
    '--branch',
    required=True,
    help='Provide branch name e.g. master')
parser.add_argument(
    '-f',
    '--filepath',
    required=True,
    help='Provide file path in repo e.g. config/settings.yaml')

args = parser.parse_args()
owner = args.owner
repo = args.repo
branch = args.branch
filepath = args.filepath

def github_read_file():
    """reads the file content from GitHub.

    Returns:
        str: file content
    """
    github_token = os.environ['GITHUB_TOKEN']
    headers = {'Authorization': 'token {}'.format(github_token)}
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{filepath}?ref={branch}'
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    data = res.json()
    file_content = data['content']
    file_content_encoding = data.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()
    return file_content

file_content = github_read_file()
print(file_content)
