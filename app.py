import sys
from typing import ContextManager
from flask import Flask, render_template

from utils import get_industrias, get_model

app = Flask(__name__)

@app.route('/', methods=['GET', ])
def home():
    
    test_data = get_model()
    industrias = get_industrias()

    
    return render_template('index.html', test_data=test_data, industrias=industrias)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, use_reloader=True)