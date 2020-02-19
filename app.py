from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  print("aaa222222")
  return 'Hello World56568886786885f222fsdfsdfsdf6!'

  # return render_template("main/index.html")


if __name__ == '__main__':
  app.run()
