# Photo Gallery & Portfolio

A professional photo gallery and portfolio application built with Python Flask and Tailwind CSS. This project is designed for **demoing GitHub Copilot features** in a real-world web application. The included demos showcase how Copilot can assist with code generation, refactoring, UI building, and more.

## Demos

- All demo guides and examples are in the [`demos/`](demos/) folder.
- For more information about each demo, refer to the [README](demos/README.md) file in the `demos/` directory.
- To get started, check out the first demo [`features-demo.md`](demos/features-demo.md) for a walkthrough of gallery features and Copilot capabilities.

### Creating a New Demo

If you want to contribute and create a new demo, follow these steps:

1. Open GitHub Copilot Chat.
2. Type the prompt `/create-copilot-demo' with an explanation of your demo idea
3. Copilot will generate a new demo file in the `demos/` directory.
4. Fill in remaining sections with detailed instructions, examples, and expected results.

After finishing the demo, don't forget this quick follow-up:

1. Add in the overview, key skills, and demo link to the [demo README](demos/README.md)

## Getting Started

### Technical Requirements

- **Python** 3.8 or newer
- **pip** (Python package manager)

### Quick Start with GitHub Codespaces

The fastest way to get started is using GitHub Codespaces:

1. Click the **"Code"** button on the GitHub repository page
2. Select the **"Codespaces"** tab
3. Click **"Create codespace on main"** (or your current branch)
4. Wait for the codespace to build and start

The codespace will automatically configure GitHub Copilot and essential VS Code extensions.

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LennartPrins/copilot-intermediate-gallery-repo.git
   cd copilot-intermediate-gallery-repo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   python app.py
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```bash
├── app.py               # Main Flask application
├── lib/                 # Mock data and utilities
├── templates/           # Jinja2 HTML templates
├── static/              # Static files and uploads
├── demos/               # Demo guides and templates
└── requirements.txt     # Python dependencies
```