from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("page2.html")

@app.route('/texture_glass')
def text_glass():
    return render_template("texture_glass.html")

@app.route('/images', methods=['GET', 'POST'])
def textured_glass():
    return render_template("images.html")

if __name__ == '__main__':
    app.run()
