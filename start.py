from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')

# IP dan port dari masing-masing Raspberry Pi
clients = [
    {"name": "Robot 1", "url": "http://192.168.1.102:5000/video_feed"},
    {"name": "Robot 2", "url": "http://192.168.1.102:5000/video_feed"},
    {"name": "Robot 3", "url": "http://192.168.1.102:5000/video_feed"},
    {"name": "Robot 4", "url": "http://192.168.1.102:5000/video_feed"},
    {"name": "Robot 5", "url": "http://192.168.1.102:5000/video_feed"},
    {"name": "Robot 6", "url": "http://192.168.1.105:5000/video_feed"},
    {"name": "Robot 7", "url": "http://192.168.1.105:5000/video_feed"},
    {"name": "Robot 8", "url": "http://192.168.1.105:5000/video_feed"},
    {"name": "Robot 9", "url": "http://192.168.1.105:5000/video_feed"},
    {"name": "Robot 10", "url": "http://192.168.1.105:5000/video_feed"},
    {"name": "Robot 11", "url": "http://192.168.1.12:5000/video_feed"},
    {"name": "Robot 12", "url": "http://192.168.1.12:5000/video_feed"},
    {"name": "Robot 13", "url": "http://192.168.1.1:5000/video_feed"},
    {"name": "Robot 14", "url": "http://192.168.1.1:5000/video_feed"},
    {"name": "Robot 15", "url": "http://192.168.1.1:5000/video_feed"},
]

@app.route('/')
def index():
    return render_template('index.html', clients=clients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
