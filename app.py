from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return f'''
    <h1>Hello from Automated CI/CD Pipeline!</h1>
    <p><strong>Version:</strong> 2.0 - Automated Deployment</p>
    <p><strong>Deployed via:</strong> GitHub Actions + AWS SSM</p>
    <p><strong>Build Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p><strong>Assignment:</strong> Automated EC2 Deployment</p>
    '''


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'version': '2.0',
        'deployment_method': 'automated',
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
