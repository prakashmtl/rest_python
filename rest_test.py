import json

from flask import Flask

#  __name__ is the way to get the import name of the place the app is defined
app = Flask(__name__)

# It navigates to localhost:5000/total/
@app.route('/total/')


def tot():
    # it produces the list of range(1,2,3)
    numbers_to_add = list(range(1, 4))
    # sums up and store it in tot
    tot = sum(numbers_to_add)
    total = {"Total":tot}
    # it returns the result as json objects into URL response
    return json.dumps(total)

if __name__ == '__main__':
    # it runs the process, actually it contains 4 parameters. others are defaulted URL(localhost),port(5000). Need to amend this now.
    app.run(debug=True)

