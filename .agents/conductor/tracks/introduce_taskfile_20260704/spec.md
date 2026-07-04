# Specification - Introduce Taskfile.yaml

## 1. Goal
Add a root `Taskfile.yaml` to standardize common local development tasks like running tests, verification checks, and linting.

## 2. Requirements
- Define a `default` task that lists all available tasks (similar to `task -a`).
- Define a `test` task that executes `uv run python -m unittest tests/test_profile.py`.
- Define a `check` task that runs tests and prepares pre-commit checks.
