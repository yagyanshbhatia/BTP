from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefgh"

codes = [
    {
        'method_name' : 'trial 1',
        'method_code' : 'print("hello there!")'
    }, 
    {
        'method_name' : 'trial 2',
        'method_code' : 'print("hello there!")'
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/demo', methods=['GET','POST'])
def demo():
    if request.method == "POST":
        query = request.form["query"]
        print(query)
    return render_template("demo.html", title = "demo", codes = codes)

if __name__=="__main__":
    app.run(debug=True)