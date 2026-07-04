# Specification - Profile Polish and Metrics Integration

## 1. Goal
Reorganize and style the GitHub Profile README (`README.md`) to follow the visual guidelines (clear hierarchy, dark mode alignment, badges, metrics charts). Ensure all referenced SVGs are generated/updated correctly via GitHub Actions and that the repository has an automated validation script.

## 2. Requirements
- **README Layout:**
  - Header banner at the top.
  - Brief intro with flat-square Shields.io badges representing skills and profiles.
  - Metrics sections in columns or styled blocks.
  - Active contribution calendar (`iso-calender.svg`) and coding activity (`metrics-plugin-wakatime.svg`).
  - Achievements and badges (`achievements.svg`).
- **Automation and Validation:**
  - Validate that all SVGs referenced in `README.md` actually exist in the `images/` directory.
  - Validate that the GitHub Actions workflow YAML is syntactically valid.
  - A Python-based validation/test script to enforce these checks.
