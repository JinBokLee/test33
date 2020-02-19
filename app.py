from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  print("aaa")
  return 'Hello World56568886786885f222f6!'

  # return render_template("main/index.html")


if __name__ == '__main__':
  app.run()
