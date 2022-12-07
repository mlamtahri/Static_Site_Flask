# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object

app=Flask(__name__,template_folder='templates')

@app.route('/index')
def index():
    return render_template('index.html')  # render a template
@app.route('/<path:path>')
def validations(path):
    return render_template(path) 
 
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)