from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_url_path='')

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
  return render_template('index.html')

@app.route('/vidios/<path:path>')
def vidios(path):
  return send_from_directory('vidios',path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)