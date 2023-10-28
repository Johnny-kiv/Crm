from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('panel.html',href="http://192.168.1.11:5000/1")
@app.route("/<number>")
def one(number):
    return render_template(f'tasks-descriptions/{number}.html')

if __name__ == '__main__':
    app.run("0.0.0.0")