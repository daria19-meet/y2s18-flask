from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    dancers=["Beyonce", "Ashley McEverret", "Missy Copeland"]
    return render_template("index.html", dancers=dancers, likes_same_sport=False)


if __name__ == '__main__':
   app.run(debug = True)