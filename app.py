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

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/vsai')
def vsai():
    return render_template('playing.html', player_type='AI'])

@app.route('/vsplayer')
def vsplayer():
    return render_template('playing.html', player_type='Player')

@app.route('/vsfriend')
def vsfriend():
    return render_template('playing.html', player_type='Friend')


if __name__ == '__main__':
    # Listen on all interfaces so the devcontainer / host can reach it
    app.run(host='0.0.0.0', port=8000, debug=True)