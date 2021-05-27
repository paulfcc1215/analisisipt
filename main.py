import sys
from typing import ContextManager
from flask import Flask, render_template, request

from utils import get_industrias, get_model

app = Flask(__name__)

@app.route('/', methods=['GET', ])
def home():
    return render_template('index.html')


@app.route('/graficas', methods=['GET','POST'])
def graficas():
    industrias = get_industrias()
    #if request.method=='POST':
    test_data = get_model()
    return render_template('graficas.html', test_data=test_data, industrias=industrias)