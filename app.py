from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    environment = os.environ.get('ENVIRONMENT', 'unknown')
    return render_template('index.html', environment=environment)

@app.route('/health')
def health():
    return {'status': 'healthy', 'environment': os.environ.get('ENVIRONMENT', 'unknown')}

if __name__ == '__main__':
    app.run(debug=True)
