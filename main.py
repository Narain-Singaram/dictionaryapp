from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_folder='static')

df = pd.read_csv("word_table.csv")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/v1/<word>")
def api_pg(word):
    defn = df.loc[df["word"] == word]['definition'].squeeze()
    print(defn)

    return render_template("input_word.html", inp_wrd=word.capitalize(), out_defn=defn)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
