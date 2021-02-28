from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name        
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)   