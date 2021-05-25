import sys
from typing import ContextManager
from flask import Flask, render_template

from utils import get_industrias, get_model

app = Flask(__name__)

# def app(environ, start_response):
# 	test_data = get_model()
# 	industrias = get_industrias()
# 	data = str(render_template('index.html', test_data=test_data, industrias=industrias))
# 	status = '200 OK'
# 	#data=b"fer"
# 	response_headers = [
# 		('Content-type', 'text/plain'),
# 		('Content-Length', str(len(data)))
# 	]
# 	start_response(status, response_headers)
# 	return iter([data])


@app.route('/', methods=['GET', ])
def home():
    
    test_data = get_model()
    industrias = get_industrias()
    
    return render_template('index.html', test_data=test_data, industrias=industrias)

if __name__ == '__main__':
    app.run()