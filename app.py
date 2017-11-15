from flask import Flask
import os
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/certi.html')
def certi():
    return render_template("certi.html")
@app.route('/rp.html')
def rp():
    return render_template("rp.html")
@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
	#decide what port to run the app in
	port = int(os.environ.get('PORT', 5000))
	#run the app locally on the givn port
	app.run(host='0.0.0.0', port=port)
	app.run(debug=True)