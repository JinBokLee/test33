from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  print("aaa222224sdfsdf2")
  name = "JB"
  return 'Hello World56568886786885f222fsdfsdfsdf6! - {}'.format(name)

  # return render_template("main/index.html")


if __name__ == '__main__':
  app.run()
