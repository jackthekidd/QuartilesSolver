from flask import Flask, request, render_template, redirect, url_for
from solve import solve_puzzle  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tiles = ['' for _ in range(20)]
    solutions = {}

    if request.method == 'POST':
        if 'screenshot' in request.files:
            pass
        else:
            for i in range(20):
                tiles[i] = request.form.get(f'tile_{i}', '').strip().lower()
            solutions = solve_puzzle(tiles)  # returns solutions dictionary

    return render_template('index.html', tiles=tiles, solutions=solutions)

@app.route('/solve', methods=['POST'])
def solve():
    # Get corrected tiles from form
    tiles = []
    for i in range(20):
        tile = request.form.get(f'tile_{i}', '').strip().lower()
        tiles.append(tile)

    # Pass tiles to the puzzle solver
    solutions = solve_puzzle(tiles)  # adapt this to your solver

    # Render solutions page
    return render_template('solution.html', solutions=solutions)

if __name__ == '__main__':
    app.run(debug=True)
