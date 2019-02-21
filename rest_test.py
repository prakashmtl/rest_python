import json
from flask import Flask

app = Flask(__name__)

@app.route('/total/')

def tot():
    numbers_to_add = list(range(1, 4))
    tot = sum(numbers_to_add)
    total = {"Total":tot}
    return json.dumps(total)

if __name__ == '__main__':
    app.run(debug=True)

