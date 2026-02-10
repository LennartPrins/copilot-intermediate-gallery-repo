from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
from lib.mock_photo_data import photos
from lib.mock_admin_data import dashboard_stats, recent_galleries
from lib.mock_feature_card_data import feature_cards
from lib.mock_tag_data import tags

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    """Home page with hero section and feature highlights"""
    recent_photos = photos[:6]  # Show first 6 photos
    return render_template('index.html', 
                         feature_cards=feature_cards,
                         recent_photos=recent_photos)

@app.route('/gallery')
def gallery():
    """Gallery page with filtering and search"""
    selected_tag = request.args.get('tag', 'all')
    search_query = request.args.get('search', '').lower()
    
    # Filter photos
    filtered_photos = photos
    
    if selected_tag != 'all':
        filtered_photos = [p for p in filtered_photos if selected_tag in p['tags']]
    
    if search_query:
        filtered_photos = [p for p in filtered_photos 
                          if search_query in p['title'].lower() or 
                          search_query in p.get('photographer', '').lower()]
    
    return render_template('gallery.html', 
                         photos=filtered_photos,
                         tags=tags,
                         selected_tag=selected_tag,
                         search_query=search_query)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload page for adding new photos"""
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        files = request.files.getlist('files[]')
        uploaded_files = []
        
        for file in files:
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                uploaded_files.append(filename)
        
        return jsonify({'success': True, 'files': uploaded_files})
    
    return render_template('upload.html', tags=tags)

@app.route('/admin')
def admin():
    """Admin dashboard with statistics and management"""
    return render_template('admin.html',
                         stats=dashboard_stats,
                         galleries=recent_galleries)

@app.route('/api/photos/<photo_id>/like', methods=['POST'])
def like_photo(photo_id):
    """API endpoint to like a photo"""
    for photo in photos:
        if photo['id'] == photo_id:
            photo['likes'] += 1
            return jsonify({'success': True, 'likes': photo['likes']})
    return jsonify({'error': 'Photo not found'}), 404

@app.route('/api/photos/<photo_id>/download', methods=['POST'])
def download_photo(photo_id):
    """API endpoint to track photo downloads"""
    for photo in photos:
        if photo['id'] == photo_id:
            photo['downloads'] += 1
            return jsonify({'success': True, 'downloads': photo['downloads']})
    return jsonify({'error': 'Photo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
