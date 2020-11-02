from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('main-page.html')

if __name__ == '__main__':
    app.run(debug=True)