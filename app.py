from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/howtoplay')
def how_to_play():
    return render_template('howtoplay.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    # Listen on all interfaces so the devcontainer / host can reach it
    app.run(host='0.0.0.0', port=5000, debug=True)