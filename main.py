from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index(name=None):
    template = 'index.html'
    return render_template(template, name=name)

# @app.route('/labs', methods=["GET"])
# def labs(name=None):
#     template = 'labs.html'
#     return render_template(template, name=name)

if __name__ == "__main__":
    app.run()
