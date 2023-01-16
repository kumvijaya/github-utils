# GitHub Utils

This repository keeps the util scripts to interact with GitHub using python
- Connects to Github using REST API.
- For execution, This expects environment variable **GITHUB_TOKEN** to be set with valid GitHub PAT (Perosonal Access Token).

This uses [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28)

## Read file content from GitHub
This CLI/util can be used to get github file content for the given org, repo, and file path.

This module takes below parameters.

- owner -- Provide github user/owner name e.g. kumvijaya
- repo -- Provide repository name e.g. my-repo
- branch  -- Provide branch name e.g. master
- filepath  -- Provide file path in repo e.g. config/settings.yaml

Refer more details [here](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28)

