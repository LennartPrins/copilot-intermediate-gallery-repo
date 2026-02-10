# Photo Gallery & Portfolio (Python/Flask)

A professional photo gallery and portfolio application built with Python Flask. This project is designed for **demoing GitHub Copilot features** in a real-world web application.

## Features

- 📸 **Gallery browsing** with filtering by tags and search functionality
- 📤 **Photo upload** with drag-and-drop support
- 📊 **Admin dashboard** for managing galleries and viewing statistics
- 🎨 **Responsive design** with Tailwind CSS
- 🌓 **Dark mode** support

## Technical Stack

- **Backend**: Python 3.8+ with Flask
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Templates**: Jinja2
- **Image Processing**: Pillow

## Getting Started

### Prerequisites

- Python 3.8 or newer
- pip (Python package manager)

### Installation

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

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

## Project Structure

```
├── app.py                  # Main Flask application
├── lib/                    # Data and utilities
│   ├── mock_photo_data.py
│   ├── mock_tag_data.py
│   ├── mock_admin_data.py
│   └── mock_feature_card_data.py
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── gallery.html
│   ├── upload.html
│   └── admin.html
├── static/                 # Static files
│   └── uploads/           # Uploaded photos
└── requirements.txt        # Python dependencies
```

## Available Routes

- `/` - Home page with featured galleries
- `/gallery` - Browse all photos with filtering
- `/upload` - Upload new photos
- `/admin` - Admin dashboard

## API Endpoints

- `POST /api/photos/<id>/like` - Like a photo
- `POST /api/photos/<id>/download` - Track photo download

## Development

The application uses Flask's built-in development server with debug mode enabled. Any changes to Python files will automatically reload the server.

## Demos

All demo guides and examples are in the [`demos/`](demos/) folder. For more information about each demo, refer to the [README](demos/README.md) file in the `demos/` directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
