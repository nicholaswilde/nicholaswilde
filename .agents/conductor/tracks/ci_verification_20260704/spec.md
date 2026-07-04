# Specification - Configure Automated CI Verification

## 1. Goal
Configure a GitHub Actions workflow to run the profile validation test suite automatically on pushes to the `main` branch and pull requests.

## 2. Requirements
- Create a new workflow file `.github/workflows/test.yml`.
- The workflow should run on `push` to `main` and `pull_request` targeting `main`.
- The job should check out the repository, setup Python, install `uv`, and run the unittest suite.
