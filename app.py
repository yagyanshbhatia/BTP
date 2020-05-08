from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdefgh"

codes = [
    {
        'method_name' : 'trial 1',
        'method_code' : 'code here!'
    }, 
    {
        'method_name' : 'trial 2',
        'method_code' : 'print("hello there!")'
    }
]

@app.route('/')
def index():
    return render_template("index.html")

def update_codes(query):
    # Note For Akhil Chandra
    # This is where you update the rank list : codes 
    # after the search is done, query is the search string. 
    global codes
    codes.append({
        'method_name':query,
        'method_code':'int main()'
    })
    return codes

@app.route('/demo', methods=['GET','POST'])
def demo():
    global codes
    if request.method == "POST":
        query = request.form["query"]
        codes = update_codes(query)
    return render_template("demo.html", title = "demo", code = codes, len = len(codes))

if __name__=="__main__":
    app.run(debug=True)