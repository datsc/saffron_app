from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "hello test3 world!"

if __name__=="__main__":
    app.run("0.0.0.0")
