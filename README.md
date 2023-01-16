# GitHub Utils

This repository keeps the util scripts to interact with GitHub using python
- Connects to Github using REST API.
- For execution, This expects environment variable **GITHUB_TOKEN** to be set with valid GitHub PAT (Perosonal Access Token).

This uses [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28)

## Read file content from GitHub
This CLI/util can used to get github file content for the given org, repo, and file path.

This module takes below parameters.
- org -- GitHub org (Example: kumvijaya)
- repo -- Repository name (Example: test-repo)
- path -- File path in the repo (Example: folder1/test.yaml)

Refer more details [here](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28)

