from flask import Flask, render_template, request, redirect, url_for
import os, json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
DATA_FILE = 'data/content.json'

def load_content():
    if not os.path.exists(DATA_FILE):
        return {
            "hero": {
                "title": "",
                "chapter": "",
            },
            "hero_carousel1": "",
            "hero_carousel2": "",
            "hero_carousel3": "",
            "video": {
                "url": ""
            }
        }
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_content(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    data = load_content()
    return render_template('index.html', data=data)


@app.route('/aboutus')
def aboutus():
    data = load_content()
    return render_template('aboutus.html', data=data)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    data = load_content()

    # Pastikan struktur lengkap
    data.setdefault('hero', {}).setdefault('title', '')
    data['hero'].setdefault('chapter', '')
    data['hero'].setdefault('description', '')
    data['hero'].setdefault('image', '')
    for i in range(1, 4):
        data.setdefault(f'hero_carousel{i}', '')
    data.setdefault('video', {}).setdefault('url', '')

    if request.method == 'POST':
        # Teks Hero
        data['hero']['title'] = request.form.get('hero_title', '')
        data['hero']['chapter'] = request.form.get('hero_chapter', '')
        data['hero']['description'] = request.form.get('hero_description', '')

        # Gambar Hero
        hero_image = request.files.get('hero_image')
        if hero_image and hero_image.filename:
            filename = secure_filename(hero_image.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            hero_image.save(path)
            data['hero']['image'] = f"uploads/{filename}"

        # Carousel Images
        for i in range(1, 4):
            carousel_file = request.files.get(f'hero_carousel{i}')
            if carousel_file and carousel_file.filename:
                filename = secure_filename(carousel_file.filename)
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                carousel_file.save(path)
                data[f'hero_carousel{i}'] = f"uploads/{filename}"

        # Video Upload
        # Upload video
        video_file = request.files.get('video_url')
        if video_file and video_file.filename:
            filename = secure_filename(video_file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            video_file.save(path)
            data['video']['url'] = f"uploads/{filename}"


        save_content(data)
        return redirect(url_for('admin'))

    return render_template('admin.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
