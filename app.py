from flask import Flask
# flask is the module with small f letter and Flask is the class of this module with capital F and now we will create an object for this class as python is a object oriented programming language.

app = Flask(__name__)

@app.route("/")
def hello():
  return "hello world"


if __name__ == '__main__':
 app.run(host='0.0.0.0' , debug=True)