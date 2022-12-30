from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index_pg():
    return render_template("index.html")
@app.route("/api/v1/<word>")
def api_pg(word):
    definition = word.upper()
    result_dictionary = {"word": word, 'definition': definition}
    return result_dictionary

if(__name__ == "__main__"):
    app.run(debug=True,port=5001)