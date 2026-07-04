# Tech Stack - GitHub Profile & Metrics Display

## 1. Platform & Hosting
- **GitHub Profile:** The primary hosting platform for the profile page (`nicholaswilde/nicholaswilde`).

## 2. Automation & Workflow
- **GitHub Actions:** CI/CD runner to automate execution of metrics updates.
- **lowlighter/metrics:** GitHub Action used to fetch statistics, generate SVGs, and automatically commit them to the repository.
- **go-task (Taskfile):** Task runner to standardize common development tasks (e.g. running tests locally).

## 3. Formats & Markup
- **Markdown (GFM):** Document format for `README.md`.
- **SVG (Scalable Vector Graphics):** High-resolution, vector-based graphics format for all status charts, contribution calendars, and WakaTime metrics.

## 4. APIs & Integrations
- **GitHub API:** To fetch contribution history, repository details, achievements, and follow-up metrics.
- **WakaTime API:** To retrieve coding activity, editor preference, language distributions, and operating system stats.

## 5. Security & Secrets Management
- **GitHub Repository Secrets:**
  - `METRICS_SECRET`: Personal Access Token (PAT) with read permissions for user metrics.
  - `GITHUB_TOKEN`: Standard repository token used by actions to commit generated SVGs back to the repo.
  - `USER_TIMEZONE`: Timezone parameter for local time metric calculations.
  - `WAKATIME_API_KEY`: API key for accessing WakaTime metrics.

## 6. Local Validation & Testing
- **uv:** Fast Python package installer and runner, used to run the validation test suite local to the developer's machine (`uv run python -m unittest ...`).

