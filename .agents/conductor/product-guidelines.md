# Product Guidelines

## 1. Style & Tone
- **Professional & Clean:** Keep descriptions, project details, and status updates professional, clear, and direct.
- **Action-Oriented:** Focus on achievements, technologies used, and metrics rather than generic descriptions.
- **Minimalist:** Let the metrics and charts speak for themselves. Avoid long blocks of text.

## 2. Branding & Aesthetic Guidelines
- **Theme:** Strict dark mode aesthetic to match GitHub's default dark theme.
- **Color Palette:**
  - Backgrounds: Dark slate/gray (#0d1117, #0d0f12).
  - Accents: Dynamic colors representing language statistics (e.g. GitHub language colors).
  - Highlights: Sleek blues, cyans, and purples to emphasize active stats.
- **Banners and SVG Graphics:**
  - Banners should have a professional aspect ratio (e.g., 3:1).
  - SVGs should use vector shapes and standard system or web-safe fonts (like Inter, Segoe UI, system-ui) to render correctly across all devices.

## 3. Layout & Organization Guidelines
- **Visual Hierarchy:** Place the most critical and impressive metrics (e.g., top repositories, total coding hours) near the top.
- **Section Ordering:**
  1. Header/Banner
  2. Brief introduction & skills overview
  3. Metric badges & contribution statistics
  4. Top/pinned repositories
  5. Coding activity & habits charts
- **Badges:** Use flat/clean badges (like Shields.io shields) with consistent styles (e.g. flat-square or for-the-badge) and matching colors.

## 4. Technical Quality Guidelines
- **Valid Markdown:** Ensure all markdown files are clean, validate without warnings, and use correct formatting.
- **Image Paths:** Use relative paths or reliable GitHub-hosted links for images/SVGs to prevent broken assets.
- **Automation Reliability:** Ensure any scripts that update SVGs run robustly via GitHub Actions without breaking changes.
