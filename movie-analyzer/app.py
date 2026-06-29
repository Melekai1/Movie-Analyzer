from flask import Flask, render_template, jsonify  # type: ignore[import]
import csv

app = Flask(__name__)

def load_movies():
    movies = []
    with open("movies.csv", "r") as f:
        reader = csv.DictReader(f);
        for row in reader:
            movies.append(row)
    return movies

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/movies") 
def get_movies():
    movies = load_movies()
    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True)
    

